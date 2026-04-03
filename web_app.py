import random
import string
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room, leave_room
from RPSBattle import moveviachar, turnOccurence, genericpick, attributize


_CUSTOM_MOVE_DESCRIPTIONS = {
    # Jepr (char 1)
    't': 'Taunt. Doubles next damage dealt.',
    # Poxx (char 4, v3)
    'v3a2': 'Light attack. Deals 2 damage. Turns off shield effects.',
    'v3t':  'Taunt. Gain 1 Charge. Lose 2 HP first time playing. Gain 3 Charge to deal 25 damage.',
    'v2a1': 'Strong attack. Deals 10 damage. Lose 1 HP if blocked.',
    'v2a2': 'Light attack. Deals 4 damage. Loses to Light.',
    'v2g':  'Grab. Gain +2 block boost.',
    'v2t':  'Taunt. Block boost is used to boost your next damage dealt.',
    # Zephyr (char 6, v5)
    'v5a1': 'Strong attack. Deals 5 damage. Beats other strong attacks.',
    'v4a2': 'Light attack. Deals 2 damage. Against taunt deals double damage. Your next heal is tripled.',
    'v4g':  'Grab. Deals 7 damage. Lifesteal -1.',
    'v4t':  'Taunt. Converts heal into damage.',
}


def describe_move(move_code):
    """Return a human-readable tooltip for a move code."""
    if move_code in _CUSTOM_MOVE_DESCRIPTIONS:
        return _CUSTOM_MOVE_DESCRIPTIONS[move_code]
    (attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue,
     lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster,
     blockability, tauntkiller, shieldnegate, remover, strongmultiplier,
     tauntincrement, tradeheal, healattribute, grabweakness, grabattribute,
     healconattribute, healcounter, hitlessheal, tauntvtauntdamage,
     armormultiplierattribute, armorgain, armorattack, counterbonus,
     tauntnegation, preventattribute) = attributize(move_code)

    type_label = {
        'strong':  'Strong attack',
        'light':   'Light attack',
        'shield':  'Shield / block',
        'counter': 'Counter',
        'grab':    'Grab',
        'taunt':   'Taunt',
        'pass':    'Pass (skip turn)',
    }.get(attacktype, attacktype.capitalize())

    parts = [type_label]

    if damage > 0:
        parts.append(f'Deals {damage} damage')
    if lifeheal > 0:
        parts.append(f'Heals {lifeheal} HP')
    elif lifeheal < 0:
        parts.append(f'Costs {abs(lifeheal)} HP to use')
    if hitlessheal > 0:
        parts.append(f'Heals {hitlessheal} HP passively')
    if lifedrain > 0:
        parts.append(f'Drains {lifedrain} HP from opponent')
    if tradeheal > 0:
        parts.append(f'Heals {tradeheal} HP when trades occur')
    if seedincrement > 0:
        parts.append(f'Gains {seedincrement} Seed')
    if armorgain > 0:
        parts.append(f'Gains {armorgain} armor')
    if armorattack > 0:
        parts.append('Converts armor into damage when attacking')
    if armormultiplierattribute > 1:
        parts.append(f'Next armor gain is multiplied by x{armormultiplierattribute}')
    if blockpenalty > 0:
        parts.append('Deals extra damage through shields')
    if blockbooster > 0:
        parts.append(f'Boosts block power by +{blockbooster}')
    if blockability > 0:
        parts.append('Unlocks shield blocking ability')
    if remover > 0:
        parts.append("Locks opponent's strong and light moves")
    if shieldnegate > 0:
        parts.append('Pierces shields')
    if tauntkiller > 1:
        parts.append(f'Extra effective vs Taunt (x{tauntkiller})')
    elif tauntkiller == 0:
        parts.append('Deals no damage vs Taunt')
    if countervalue > 0:
        parts.append(f'Reflects incoming strong/light x{countervalue}')
    if strongmultiplier > 1:
        parts.append(f'Counter multiplier x{strongmultiplier} vs strong')
    elif 0 < strongmultiplier < 1:
        from fractions import Fraction
        frac = Fraction(strongmultiplier).limit_denominator(10)
        parts.append(f'Only deals {frac}x damage vs strong')
    if counterbonus > 0:
        parts.append(f'Takes {counterbonus} bonus damage from counters')
    if healcounter > 0:
        parts.append('Heals when landing a counter hit')
    if tauntincrement > 0:
        parts.append('Builds taunt charge each use')
    if tauntvtauntdamage > 0:
        parts.append(f'Deals {tauntvtauntdamage} damage if both players taunt')
    if tauntnegation > 0:
        parts.append('Negates all taunt effects')
    if grabattribute > 1:
        parts.append(f'Next grab deals {grabattribute}x damage')
    if move_code == 'v3g':
        parts.append('Beats opposing grabs')
    if healattribute > 1:
        parts.append(f'Multiplies heals by x{healattribute}')
    if healconattribute > 0:
        parts.append('Converts heal into damage on condition')
    if preventattribute == 0:
        parts.append("Prevents next damage taken")
    if counterweakness > 1:
        parts.append(f'Takes x{counterweakness} damage from counters')

    return '. '.join(parts) + '.'

app = Flask(__name__)
app.secret_key = 'rpsbattle-local-key'

socketio = SocketIO(app, cors_allowed_origins="*")

CHARACTER_NAMES = {
    1: 'Jepr',
    2: 'Seed Guy',
    3: 'Hair',
    4: 'Poxx',
    5: 'Gbomb',
    6: 'Zephyr',
    7: 'Cornelius',
    8: 'C',
}

CHARACTER_IMAGES = {
    1: 'Jepr.png',
    2: 'Seed_Guy.png',
    3: 'Hair.png',
    4: 'Poxx.png',
    5: 'GBomb.png',
    6: 'Zephyr.png',
    7: 'Cornelius.png',
    8: 'C.png',
}

MOVE_LABELS = ['Strong', 'Light', 'Shield', 'Counter', 'Grab', 'Taunt']

# ── Room-based game state ──
rooms = {}
# Maps socket sid -> room_id for disconnect handling
sid_to_room = {}
# Pending disconnect timers: (room_id, player_num) -> greenlet
_disconnect_timers = {}


def generate_room_code():
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if code not in rooms:
            return code


def new_game_state(char1, char2, bot_play):
    return {
        'char1': char1,
        'char2': char2,
        'bot_play': bot_play,
        'pickslist1': moveviachar(char1),
        'pickslist2': moveviachar(char2),
        'k1': 25, 'k2': 25,
        'p1win': 0, 'p2win': 0,
        'counter': 0, 'tracker': 0,
        'p1health': 25, 'p2health': 25,
        'tauntboost': 1, 'tauntboost2': 1,
        'seedcount': 0, 'seedcount2': 0,
        'blockboost': 0, 'blockboost2': 0,
        'trueblockability': 0, 'trueblockability2': 0,
        'removera1': 0, 'removera2': 0, 'removera12': 0, 'removera22': 0,
        'gametracker': 0, 'wasted': 0,
        'tauntvalue': 0, 'tauntvalue2': 0,
        'healmultiplier': 1, 'healmultiplier2': 1,
        'grabmultiplier': 1, 'grabmultiplier2': 1,
        'healcon': 0, 'healcon2': 0,
        'armormultiplier': 1, 'armormultiplier2': 1,
        'armor': 0, 'armor2': 0,
        'prevent': 1, 'prevent2': 1,
        'game_over': False,
        'winner': 0,
        'last_p1move': '',
        'last_p2move': '',
    }


def get_attributes(gs):
    """Return character-specific attribute values for display."""
    char1 = gs['char1']
    char2 = gs['char2']
    attrs1 = {}
    attrs2 = {}
    if char1 == 1:
        attrs1 = {'Tauntboost': gs['tauntboost']}
    elif char1 == 2:
        attrs1 = {'Seed count': gs['seedcount']}
    elif char1 == 3:
        attrs1 = {'Blockability': gs['trueblockability'], 'Block boost': gs['blockboost']}
    elif char1 == 4:
        attrs1 = {'Taunt value': gs['tauntvalue'], 'Remover strong': gs['removera12'], 'Remover fast': gs['removera22']}
    elif char1 == 5:
        attrs1 = {'Heal condition': gs['healcon'], 'Heal multiplier': gs['healmultiplier']}
    elif char1 == 6:
        attrs1 = {'Grab multiplier': gs['grabmultiplier']}
    elif char1 == 7:
        attrs1 = {'Armor': gs['armor'], 'Armor multiplier': gs['armormultiplier']}
    elif char1 == 8:
        attrs1 = {'Prevent': gs['prevent']}

    if char2 == 1:
        attrs2 = {'Tauntboost': gs['tauntboost2']}
    elif char2 == 2:
        attrs2 = {'Seed count': gs['seedcount2']}
    elif char2 == 3:
        attrs2 = {'Blockability': gs['trueblockability2'], 'Block boost': gs['blockboost2']}
    elif char2 == 4:
        attrs2 = {'Taunt value': gs['tauntvalue2'], 'Remover strong': gs['removera1'], 'Remover fast': gs['removera2']}
    elif char2 == 5:
        attrs2 = {'Heal condition': gs['healcon2'], 'Heal multiplier': gs['healmultiplier2']}
    elif char2 == 6:
        attrs2 = {'Grab multiplier': gs['grabmultiplier2']}
    elif char2 == 7:
        attrs2 = {'Armor': gs['armor2'], 'Armor multiplier': gs['armormultiplier2']}
    elif char2 == 8:
        attrs2 = {'Prevent': gs['prevent2']}

    return attrs1, attrs2


def narrate_round(name1, name2, pick1, pick2, prev_p1hp, prev_p2hp, new_p1hp, new_p2hp, wasted):
    """Return a plain-English description of what just happened in a round."""
    a1 = attributize(pick1)
    a2 = attributize(pick2)
    type1, spd1, dmg1 = a1[0], a1[1], a1[2]
    type2, spd2, dmg2 = a2[0], a2[1], a2[2]

    p1hp = max(0, new_p1hp)
    p2hp = max(0, new_p2hp)
    p1dmg_taken = prev_p1hp - p1hp
    p2dmg_taken = prev_p2hp - p2hp
    p1healed = max(0, p1hp - prev_p1hp)
    p2healed = max(0, p2hp - prev_p2hp)

    type_word = {
        'strong': 'a strong attack', 'light': 'a light attack',
        'shield': 'a shield',        'counter': 'a counter',
        'grab':   'a grab',          'taunt': 'a taunt',
        'pass':   'a pass',
    }

    lines = []
    lines.append(f"{name1} used {type_word.get(type1, type1)} — {name2} used {type_word.get(type2, type2)}.")

    if wasted:
        lines.append("The move was blocked or nullified — the turn was wasted!")
    else:
        if type1 == 'shield' and type2 in ('strong', 'light', 'grab') and p1dmg_taken == 0:
            lines.append(f"{name1}'s shield held firm, absorbing the attack.")
        elif type2 == 'shield' and type1 in ('strong', 'light', 'grab') and p2dmg_taken == 0:
            lines.append(f"{name2}'s shield held firm, absorbing the attack.")

        if type1 == 'counter' and p2dmg_taken > 0:
            lines.append(f"{name1} countered, reflecting damage back at {name2}!")
        if type2 == 'counter' and p1dmg_taken > 0:
            lines.append(f"{name2} countered, reflecting damage back at {name1}!")

        if type1 == 'grab' and p2dmg_taken > 0:
            lines.append(f"{name1} grabbed {name2} for {p2dmg_taken} damage.")
        elif type1 in ('strong', 'light') and p2dmg_taken > 0:
            lines.append(f"{name1} dealt {p2dmg_taken} damage to {name2}.")
        elif type1 == 'taunt' and p2dmg_taken > 0:
            lines.append(f"{name1}'s taunt zapped {name2} for {p2dmg_taken} damage.")

        if type2 == 'grab' and p1dmg_taken > 0:
            lines.append(f"{name2} grabbed {name1} for {p1dmg_taken} damage.")
        elif type2 in ('strong', 'light') and p1dmg_taken > 0:
            lines.append(f"{name2} dealt {p1dmg_taken} damage to {name1}.")
        elif type2 == 'taunt' and p1dmg_taken > 0:
            lines.append(f"{name2}'s taunt zapped {name1} for {p1dmg_taken} damage.")

        if p1healed > 0:
            lines.append(f"{name1} recovered {p1healed} HP.")
        if p2healed > 0:
            lines.append(f"{name2} recovered {p2healed} HP.")

        if p1dmg_taken == 0 and p2dmg_taken == 0 and p1healed == 0 and p2healed == 0:
            if type1 == 'taunt' or type2 == 'taunt':
                lines.append("Taunts charged but no immediate damage was dealt.")
            elif type1 == 'shield' or type2 == 'shield':
                lines.append("Shields were raised — no damage exchanged.")
            elif type1 == 'pass' or type2 == 'pass':
                lines.append("A turn was passed.")
            else:
                lines.append("No HP was lost this round.")

    lines.append(f"HP — {name1}: {p1hp}  |  {name2}: {p2hp}")
    return '  '.join(lines)


def state_to_json(gs, narrative=None):
    attrs1, attrs2 = get_attributes(gs)
    d = {
        'p1health': max(0, min(gs['p1health'], gs['k1'])),
        'p2health': max(0, min(gs['p2health'], gs['k2'])),
        'k1': gs['k1'],
        'k2': gs['k2'],
        'last_p1move': gs['last_p1move'],
        'last_p2move': gs['last_p2move'],
        'game_over': gs['game_over'],
        'winner': gs['winner'],
        'attrs1': attrs1,
        'attrs2': attrs2,
    }
    if narrative is not None:
        d['narrative'] = narrative
    return d


def resolve_turn(room_id):
    """Resolve a turn when both players have submitted moves."""
    room = rooms[room_id]
    gs = room['game_state']

    pick1 = gs['pickslist1'][room['pending_moves'][1]]
    if room['bot_play']:
        pick2 = random.choice(gs['pickslist2'])
    else:
        pick2 = gs['pickslist2'][room['pending_moves'][2]]

    prev_p1hp = gs['p1health']
    prev_p2hp = gs['p2health']

    (k1, k2, p1win, p2win, counter, tracker,
     p1health, p2health, tauntboost, tauntboost2,
     seedcount, seedcount2, blockboost, blockboost2,
     trueblockability, trueblockability2,
     removera1, removera2, removera12, removera22,
     gametracker, wasted, tauntvalue, tauntvalue2,
     healmultiplier, healmultiplier2,
     grabmultiplier, grabmultiplier2,
     healcon, healcon2,
     armormultiplier, armormultiplier2,
     armor, armor2,
     prevent, prevent2) = turnOccurence(
        gs['k1'], gs['k2'], gs['p1win'], gs['p2win'],
        gs['counter'], gs['tracker'],
        gs['p1health'], gs['p2health'],
        gs['tauntboost'], gs['tauntboost2'],
        gs['seedcount'], gs['seedcount2'],
        gs['blockboost'], gs['blockboost2'],
        gs['trueblockability'], gs['trueblockability2'],
        gs['removera1'], gs['removera2'], gs['removera12'], gs['removera22'],
        gs['gametracker'], gs['wasted'],
        gs['tauntvalue'], gs['tauntvalue2'],
        gs['healmultiplier'], gs['healmultiplier2'],
        gs['grabmultiplier'], gs['grabmultiplier2'],
        gs['healcon'], gs['healcon2'],
        gs['armormultiplier'], gs['armormultiplier2'],
        gs['armor'], gs['armor2'],
        gs['prevent'], gs['prevent2'],
        pick1, pick2
    )

    gs.update({
        'k1': k1, 'k2': k2, 'p1win': p1win, 'p2win': p2win,
        'counter': counter, 'tracker': tracker,
        'p1health': p1health, 'p2health': p2health,
        'tauntboost': tauntboost, 'tauntboost2': tauntboost2,
        'seedcount': seedcount, 'seedcount2': seedcount2,
        'blockboost': blockboost, 'blockboost2': blockboost2,
        'trueblockability': trueblockability, 'trueblockability2': trueblockability2,
        'removera1': removera1, 'removera2': removera2,
        'removera12': removera12, 'removera22': removera22,
        'gametracker': gametracker, 'wasted': wasted,
        'tauntvalue': tauntvalue, 'tauntvalue2': tauntvalue2,
        'healmultiplier': healmultiplier, 'healmultiplier2': healmultiplier2,
        'grabmultiplier': grabmultiplier, 'grabmultiplier2': grabmultiplier2,
        'healcon': healcon, 'healcon2': healcon2,
        'armormultiplier': armormultiplier, 'armormultiplier2': armormultiplier2,
        'armor': armor, 'armor2': armor2,
        'prevent': prevent, 'prevent2': prevent2,
        'last_p1move': pick1,
        'last_p2move': pick2,
    })

    if p1win or p2win:
        gs['game_over'] = True
        if p1win and p2win:
            gs['winner'] = 0
        elif p1win:
            gs['winner'] = 1
        else:
            gs['winner'] = 2

    name1 = CHARACTER_NAMES[gs['char1']]
    name2 = CHARACTER_NAMES[gs['char2']]
    narrative = narrate_round(name1, name2, pick1, pick2,
                              prev_p1hp, prev_p2hp,
                              min(gs['p1health'], gs['k1']),
                              min(gs['p2health'], gs['k2']),
                              wasted)

    room['pending_moves'] = {1: None, 2: None}
    result = state_to_json(gs, narrative=narrative)
    socketio.emit('turn_result', result, room=room_id)


# ── Flask Routes ──

@app.route('/')
def index():
    return render_template('lobby.html')


@app.route('/create-room', methods=['POST'])
def create_room():
    room_id = generate_room_code()
    bot_play = request.form.get('bot_play') == 'on'
    rooms[room_id] = {
        'game_state': None,
        'players': {},  # player_num -> sid
        'chars': {1: None, 2: None},
        'phase': 'char_select' if bot_play else 'waiting',
        'bot_play': bot_play,
        'pending_moves': {1: None, 2: None},
    }
    session['room_id'] = room_id
    session['player_num'] = 1
    return redirect(url_for('char_select', room_id=room_id))


@app.route('/join-room', methods=['POST'])
def join_room_route():
    room_id = request.form.get('room_code', '').strip().upper()
    if room_id not in rooms:
        return render_template('lobby.html', error='Room not found.')
    room = rooms[room_id]
    if room['phase'] != 'waiting':
        return render_template('lobby.html', error='Room is full or game already started.')
    session['room_id'] = room_id
    session['player_num'] = 2
    room['phase'] = 'char_select'
    # Notify P1 that opponent joined
    p1_sid = room['players'].get(1)
    if p1_sid:
        socketio.emit('opponent_joined', {}, room=p1_sid)
    return redirect(url_for('char_select', room_id=room_id))


@app.route('/room/<room_id>')
def char_select(room_id):
    if room_id not in rooms:
        return redirect(url_for('index'))
    player_num = session.get('player_num', 1)
    room = rooms[room_id]
    return render_template('char_select.html',
                           room_id=room_id,
                           player_num=player_num,
                           bot_play=room['bot_play'],
                           characters=CHARACTER_NAMES,
                           char_images=CHARACTER_IMAGES)


@app.route('/game/<room_id>')
def game(room_id):
    if room_id not in rooms or rooms[room_id]['game_state'] is None:
        return redirect(url_for('index'))
    room = rooms[room_id]
    gs = room['game_state']
    player_num = session.get('player_num', 1)
    attrs1, attrs2 = get_attributes(gs)
    return render_template(
        'game.html',
        room_id=room_id,
        player_num=player_num,
        char1_name=CHARACTER_NAMES[gs['char1']],
        char2_name=CHARACTER_NAMES[gs['char2']],
        char1_image=CHARACTER_IMAGES[gs['char1']],
        char2_image=CHARACTER_IMAGES[gs['char2']],
        move_labels=MOVE_LABELS,
        bot_play=room['bot_play'],
        state=state_to_json(gs),
        attrs1=attrs1,
        attrs2=attrs2,
        state_char1=gs['char1'],
        state_char2=gs['char2'],
        tooltips1=[describe_move(m) for m in gs['pickslist1']],
        tooltips2=[describe_move(m) for m in gs['pickslist2']],
    )


@app.route('/reset')
def reset():
    room_id = session.get('room_id')
    if room_id and room_id in rooms:
        del rooms[room_id]
    session.pop('room_id', None)
    session.pop('player_num', None)
    return redirect(url_for('index'))


# ── SocketIO Events ──

@socketio.on('connect')
def handle_connect():
    room_id = session.get('room_id')
    player_num = session.get('player_num')
    if room_id and room_id in rooms:
        join_room(room_id)
        rooms[room_id]['players'][player_num] = request.sid
        sid_to_room[request.sid] = (room_id, player_num)
        # Cancel any pending disconnect timer for this player (page navigation)
        key = (room_id, player_num)
        timer = _disconnect_timers.pop(key, None)
        if timer is not None:
            timer.cancel()


@socketio.on('disconnect')
def handle_disconnect():
    import eventlet
    info = sid_to_room.pop(request.sid, None)
    if not info:
        return
    room_id, player_num = info

    def _fire_disconnect():
        _disconnect_timers.pop((room_id, player_num), None)
        if room_id not in rooms:
            return
        room = rooms[room_id]
        # Only fire if player hasn't reconnected with a new sid
        if player_num in room['players'] and room['players'][player_num] != request.sid:
            return  # Player reconnected on a new socket
        room['players'].pop(player_num, None)
        socketio.emit('opponent_disconnected', {}, room=room_id)

    # Grace period: wait 3 seconds before notifying (covers page navigations)
    key = (room_id, player_num)
    _disconnect_timers[key] = eventlet.spawn_after(3, _fire_disconnect)


@socketio.on('select_character')
def handle_select_character(data):
    room_id = session.get('room_id')
    player_num = session.get('player_num')
    if not room_id or room_id not in rooms:
        return
    room = rooms[room_id]
    char_id = int(data.get('char_id', 1))

    if room['bot_play'] and player_num == 1:
        # P1 picks both characters in bot mode
        char2_id = int(data.get('char2_id', 1))
        room['chars'][1] = char_id
        room['chars'][2] = char2_id
    else:
        room['chars'][player_num] = char_id

    # Check if both characters are selected
    if room['chars'][1] is not None and room['chars'][2] is not None:
        gs = new_game_state(room['chars'][1], room['chars'][2], room['bot_play'])
        room['game_state'] = gs
        room['phase'] = 'playing'
        socketio.emit('both_ready', {'room_id': room_id}, room=room_id)
    else:
        # Notify opponent that this player has picked
        socketio.emit('opponent_picked', {}, room=room_id)


@socketio.on('submit_move')
def handle_submit_move(data):
    room_id = session.get('room_id')
    player_num = session.get('player_num')
    if not room_id or room_id not in rooms:
        return
    room = rooms[room_id]
    gs = room['game_state']
    if not gs or gs['game_over']:
        return

    move_idx = int(data.get('move_idx', 0))
    room['pending_moves'][player_num] = move_idx

    # Confirm to this player only
    emit('move_received', {})

    if room['bot_play'] and player_num == 1:
        # Resolve immediately with bot move
        resolve_turn(room_id)
    elif room['pending_moves'][1] is not None and room['pending_moves'][2] is not None:
        resolve_turn(room_id)


@socketio.on('request_rematch')
def handle_rematch():
    room_id = session.get('room_id')
    if not room_id or room_id not in rooms:
        return
    room = rooms[room_id]
    gs = new_game_state(room['chars'][1], room['chars'][2], room['bot_play'])
    room['game_state'] = gs
    room['pending_moves'] = {1: None, 2: None}
    result = state_to_json(gs)
    socketio.emit('game_reset', result, room=room_id)


@socketio.on('change_character')
def handle_change_character():
    room_id = session.get('room_id')
    if not room_id or room_id not in rooms:
        return
    room = rooms[room_id]
    room['game_state'] = None
    room['chars'] = {1: None, 2: None}
    room['pending_moves'] = {1: None, 2: None}
    room['phase'] = 'char_select'
    socketio.emit('go_char_select', {'room_id': room_id}, room=room_id)


if __name__ == '__main__':
    print("Starting FighterGame web server at http://0.0.0.0:5000")
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
