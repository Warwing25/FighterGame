import random
import time
from graphics import *
def gameend(player1, player2, p1win, p2win):
    if player1 < 1 and player2 < 1:
        return (p1win), (p2win)
    if player1 < 1:
        return (p1win), (p2win+1)
    if player2 < 1:
        return (p1win+1), p2win
    else:
        return p1win, p2win


def gameendwind(player1,player2):
    if player1 < 1 and player2 < 1:
        return 1, 1
    if player1 < 1:
        return 0, 1
    if player2 < 1:
        return 1, 0
    else:
        return 0, 0


def realplayerpick():
    return input("pick a move")

def picktable():
    print("Characters are:\nJepr\nSeed Guy\nHair\nPoxx\nidk\nZephyr\nCornelius\nC")
    k = input("Pick a player")
    if k == "Jepr":
        return 1
    if k == "Seed Guy":
        return 2
    if k == "Hair":
        return 3
    if k == "Poxx":
        return 4
    if k == "idk":
        return 5
    if k == "Zephyr":
        return 6
    if k == "Cornelius":
        return 7
    if k == "C":
        return 8
    return picktable()

def moveviachar(integer):
    if integer == 1:
        return ["a1", "a2", "b1", "b2", "g", "t"]
    if integer == 2:
        return ["v1a1", "v1a2", "v1b1", "v1b2", "v1g", "v1t"]
    if integer == 3:
        return ["v2a1", "v2a2", "v2b1", "v2b2", "v2g", "v2t"]
    if integer == 4:
        return ["v3a1", "v3a2", "v3b1", "v3b2", "v3g", "v3t"]
    if integer == 5:
        return ["v4a1", "v4a2", "v4b1", "v4b2", "v4g", "v4t"]
    if integer == 6:
        return ["v5a1", "v5a2", "v5b1", "v5b2", "v5g", "v5t"]
    if integer == 7:
        return ["v6a1", "v6a2", "v6b1", "v6b2", "v6g", "v6t"]
    if integer == 8:
        return ["v7a1", "v7a2", "v7b1", "v7b2", "v7g", "v7t"]
    else:
        return moveviachar(picktable())


def wastecheck(wasted, removera1, removera2, removera12, removera22, remover, remover2, static1, static2, static3, static4):
    if wasted == 1:
        return removera1, removera2, removera12, removera22
    if static1 == 1:
        removera1 = 0
        return removera1, removera2, removera12, removera22
    if static2 == 1:
        removera2 = 0
        return removera1, removera2, removera12, removera22
    if static3 == 1:
        removera12 = 0
        return removera1, removera2, removera12, removera22
    if static4 == 1:
        removera22 = 0
        return removera1, removera2, removera12, removera22

    return removera1, removera2, removera12, removera22

def healthtoarmorswitch(prep1, prep2, p1health, p2health, armor, armor2):
    if armor != 0:
        var1 = prep1 - p1health
        if var1 >= 0:
            armor = armor - var1
            p1health = p1health + var1
            if armor < 0:
                p1health = p1health + armor
                armor = 0
    if armor2 != 0:
        var2 = prep2 - p2health
        if var2 >= 0:
            armor2 = armor2 - var2
            p2health = p2health + var2
            if armor2 < 0:
                p2health = p2health + armor2
                armor2 = 0
    return p1health, p2health, armor, armor2


def window(BotPlay):
    WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
    pickslist1 = moveviachar(picktable())
    pickslist2 = moveviachar(picktable())
    k1 = 25
    k2 = 25
    p1win = 0
    p2win = 0
    counter = 0
    tracker = 0
    p1health = k1
    p2health = k2
    tauntboost = 1
    tauntboost2 = 1
    seedcount = 0
    seedcount2 = 0
    blockboost = 0
    blockboost2 = 0
    trueblockability = 0
    trueblockability2 = 0
    removera1 = 0
    removera2 = 0
    removera12 = 0
    removera22 = 0
    gametracker = 0
    wasted = 0
    tauntvalue = 0
    tauntvalue2 = 0
    healmultiplier = 1
    healmultiplier2 = 1
    grabmultiplier = 1
    grabmultiplier2 = 1
    healcon = 0
    healcon2 = 0
    armormultiplier = 1
    armormultiplier2 = 1
    armor = 0
    armor2 = 0
    prevent = 1
    prevent2 = 1
    print("occ")
    win = GraphWin("FighterGame", WINDOW_WIDTH, WINDOW_HEIGHT)
    left, left2, left3, left4, left5, left6, right, right2, right3, right4, right5, right6, quit = buttons(win)
    print("occ2")
    centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
    p1movePoint = Point(270, 360)
    p2movePoint = Point(530, 360)
    p1healthtext = Point(30, 10)
    p2healthtext = Point(770, 10)
    wintext1 = Point(350,200)
    wintext2 = Point(350, 250)
    texthealth1 = Text(p1healthtext, str(p1health))
    texthealth2 = Text(p2healthtext, str(p2health))
    text = Text(centerPoint, "")
    textm1 = Text(p1movePoint, "")
    textm2 = Text(p2movePoint, "")
    textwin1 = Text(wintext1, "Congrats, player 1 wins!!")
    textwin2 = Text(wintext2, "Congrats, player 2 wins!!")
    text.draw(win)
    textm1.draw(win)
    textm2.draw(win)
    texthealth1.draw(win)
    texthealth2.draw(win)
    cval1 = 0
    cval2 = 0
    waitloop = 0
    point1 = Point(70, 500)
    point2 = Point(70, 530)
    point3 = Point(70, 560)
    point4 = Point(730,500)
    point5 = Point(730,530)
    point6 = Point(730,560)
    textp1attribute1 = Text(point1, "")
    textp1attribute2 = Text(point2, "")
    textp1attribute3 = Text(point3, "")
    textp2attribute1 = Text(point4, "")
    textp2attribute2 = Text(point5, "")
    textp2attribute3 = Text(point6, "")
    textp1attribute1.draw(win)
    textp1attribute2.draw(win)
    textp1attribute3.draw(win)
    textp2attribute1.draw(win)
    textp2attribute2.draw(win)
    textp2attribute3.draw(win)
    if pickslist1[0] == "a1":
        textp1attribute1.setText("Tauntboost is " + str(tauntboost))
    if pickslist1[0] == "v1a1":
        textp1attribute1.setText("Seed count is " + str(seedcount))
    if pickslist1[0] == "v2a1":
        textp1attribute1.setText("Blockability is " + str(trueblockability))
    if pickslist1[0] == "v2a1":
        textp1attribute2.setText("Block boost is " + str(blockboost))
    if pickslist1[0] == "v3a1":
        textp1attribute1.setText("Taunt value is " + str(tauntvalue))
    if pickslist1[0] == "v3a1":
        textp1attribute2.setText("Remover strong is " + str(removera12))
    if pickslist1[0] == "v3a1":
        textp1attribute3.setText("Remover fast is  " + str(removera22))
    if pickslist1[0] == "v4a1":
        textp1attribute1.setText("Heal condition is " + str(healcon))
    if pickslist1[0] == "v4a1":
        textp1attribute2.setText("Heal multiplier is " + str(healmultiplier))
    if pickslist1[0] == "v5a1":
        textp1attribute1.setText("Grab multiplier is " + str(grabmultiplier))
    if pickslist1[0] == "v6a1":
        textp1attribute1.setText("Armor is " + str(armor))
    if pickslist1[0] == "v6a1":
        textp1attribute2.setText("Armor multiplier is " + str(armormultiplier))
    if pickslist1[0] == "v7a1":
        textp1attribute1.setText("Prevent value is " + str(prevent))
        
    if pickslist2[0] == "a1":
        textp2attribute1.setText("Tauntboost is " + str(tauntboost2))
    if pickslist2[0] == "v1a1":
        textp2attribute1.setText("Seed count is " + str(seedcount2))
    if pickslist2[0] == "v2a1":
        textp2attribute1.setText("Blockability is " + str(trueblockability2))
    if pickslist2[0] == "v2a1":
        textp2attribute2.setText("Block boost is " + str(blockboost2))
    if pickslist2[0] == "v3a1":
        textp2attribute1.setText("Taunt value is " + str(tauntvalue2))
    if pickslist2[0] == "v3a1":
        textp2attribute2.setText("Remover strong is " + str(removera1))
    if pickslist2[0] == "v3a1":
        textp2attribute3.setText("Remover fast is  " + str(removera2))
    if pickslist2[0] == "v4a1":
        textp2attribute1.setText("Heal condition is " + str(healcon2))
    if pickslist2[0] == "v4a1":
        textp2attribute2.setText("Heal multiplier is " + str(healmultiplier2))
    if pickslist2[0] == "v5a1":
        textp2attribute1.setText("Grab multiplier is " + str(grabmultiplier2))
    if pickslist2[0] == "v6a1":
        textp2attribute1.setText("Armor is " + str(armor2))
    if pickslist2[0] == "v6a1":
        textp2attribute2.setText("Armor multiplier is " + str(armormultiplier2))
    if pickslist2[0] == "v7a1":
        textp2attribute1.setText("Prevent value is " + str(prevent2))
    
    while True:
        clickPoint = win.getMouse()
        if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
            text.setText("")
        elif inside(clickPoint, left):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[0]
        elif inside(clickPoint, left2):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[1]
        elif inside(clickPoint, left3):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[2]
        elif inside(clickPoint, left4):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[3]
        elif inside(clickPoint, left5):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[4]
        elif inside(clickPoint, left6):
            text.setText("")
            cval1 = 1
            playerpick = pickslist1[5]
        elif inside(clickPoint, right):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[0]
        elif inside(clickPoint, right2):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[1]
        elif inside(clickPoint, right3):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[2]
        elif inside(clickPoint, right4):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[3]
        elif inside(clickPoint, right5):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[4]
        elif inside(clickPoint, right6):
            text.setText("")
            cval2 = 1
            playerpick2 = pickslist2[5]
        elif inside(clickPoint, quit):
            break
        else:
            text.setText("")
        if cval1 == 1 and BotPlay == True:
            playerpick2 = random.choice(pickslist2)
            cval2 = 1

        if cval1 == 1 and cval2 == 1 and waitloop == 0:
            textm1.setText(playerpick)
            textm2.setText(playerpick2)
            cval1 = 0
            cval2 = 0
            k1, k2, p1win, p2win, counter, tracker, p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2 = turnOccurence(k1,k2,p1win,p2win,counter,tracker,p1health,p2health,tauntboost,tauntboost2,seedcount,seedcount2,blockboost,blockboost2,trueblockability,trueblockability2,removera1,removera2,removera12,removera22,gametracker,wasted,tauntvalue,tauntvalue2,healmultiplier,healmultiplier2,grabmultiplier,grabmultiplier2,healcon,healcon2,armormultiplier,armormultiplier2,armor,armor2,prevent,prevent2,playerpick,playerpick2)
            texthealth1.setText(str(p1health))
            texthealth2.setText(str(p2health))
            if pickslist1[0] == "a1":
                textp1attribute1.setText("Tauntboost is " + str(tauntboost))
            if pickslist1[0] == "v1a1":
                textp1attribute1.setText("Seed count is " + str(seedcount))
            if pickslist1[0] == "v2a1":
                textp1attribute1.setText("Blockability is " + str(trueblockability))
            if pickslist1[0] == "v2a1":
                textp1attribute2.setText("Block boost is " + str(blockboost))
            if pickslist1[0] == "v3a1":
                textp1attribute1.setText("Taunt value is " + str(tauntvalue))
            if pickslist1[0] == "v3a1":
                textp1attribute2.setText("Remover strong is " + str(removera12))
            if pickslist1[0] == "v3a1":
                textp1attribute3.setText("Remover fast is  " + str(removera22))
            if pickslist1[0] == "v4a1":
                textp1attribute1.setText("Heal condition is " + str(healcon))
            if pickslist1[0] == "v4a1":
                textp1attribute2.setText("Heal multiplier is " + str(healmultiplier))
            if pickslist1[0] == "v5a1":
                textp1attribute1.setText("Grab multiplier is " + str(grabmultiplier))
            if pickslist1[0] == "v6a1":
                textp1attribute1.setText("Armor is " + str(armor))
            if pickslist1[0] == "v6a1":
                textp1attribute2.setText("Armor multiplier is " + str(armormultiplier))
            if pickslist1[0] == "v7a1":
                textp1attribute1.setText("Prevent value is " + str(prevent))

            if pickslist2[0] == "a1":
                textp2attribute1.setText("Tauntboost is " + str(tauntboost2))
            if pickslist2[0] == "v1a1":
                textp2attribute1.setText("Seed count is " + str(seedcount2))
            if pickslist2[0] == "v2a1":
                textp2attribute1.setText("Blockability is " + str(trueblockability2))
            if pickslist2[0] == "v2a1":
                textp2attribute2.setText("Block boost is " + str(blockboost2))
            if pickslist2[0] == "v3a1":
                textp2attribute1.setText("Taunt value is " + str(tauntvalue2))
            if pickslist2[0] == "v3a1":
                textp2attribute2.setText("Remover strong is " + str(removera1))
            if pickslist2[0] == "v3a1":
                textp2attribute3.setText("Remover fast is  " + str(removera2))
            if pickslist2[0] == "v4a1":
                textp2attribute1.setText("Heal condition is " + str(healcon2))
            if pickslist2[0] == "v4a1":
                textp2attribute2.setText("Heal multiplier is " + str(healmultiplier2))
            if pickslist2[0] == "v5a1":
                textp2attribute1.setText("Grab multiplier is " + str(grabmultiplier2))
            if pickslist2[0] == "v6a1":
                textp2attribute1.setText("Armor is " + str(armor2))
            if pickslist2[0] == "v6a1":
                textp2attribute2.setText("Armor multiplier is " + str(armormultiplier2))
            if pickslist2[0] == "v7a1":
                textp2attribute1.setText("Prevent value is " + str(prevent2))
            if p1win == 1 or p2win == 1:
                if p1win == 1:
                    textwin1.draw(win)
                if p2win == 1:
                    textwin2.draw(win)
                waitloop = 1
    win.close()

def buttons(win):
    left = Rectangle(Point(25, 55), Point(95, 105))  # points are ordered ll, ur
    left2 = Rectangle(Point(25, 115), Point(95, 165))
    left3 = Rectangle(Point(25, 175), Point(95, 225))
    left4 = Rectangle(Point(25, 235), Point(95, 285))
    left5 = Rectangle(Point(25, 295), Point(95, 345))
    left6 = Rectangle(Point(25, 355), Point(95, 405))
    right = Rectangle(Point(705, 55), Point(775, 105))
    right2 = Rectangle(Point(705, 115), Point(775, 165))
    right3 = Rectangle(Point(705, 175), Point(775, 225))
    right4 = Rectangle(Point(705, 235), Point(775, 285))
    right5 = Rectangle(Point(705, 295), Point(775, 345))
    right6 = Rectangle(Point(705, 355), Point(775, 405))
    quit = Rectangle(Point(385, 566), Point(415, 596))
    left.draw(win)
    left2.draw(win)
    left3.draw(win)
    left4.draw(win)
    left5.draw(win)
    left6.draw(win)
    right.draw(win)
    right2.draw(win)
    right3.draw(win)
    right4.draw(win)
    right5.draw(win)
    right6.draw(win)
    left.setFill("red")
    text1 = Text(Point(50,80), "Strong")
    text1.draw(win)
    left2.setFill("red")
    text2 = Text(Point(50,140), "Light")
    text2.draw(win)
    left3.setFill("red")
    text3 = Text(Point(50,200), "Shield")
    text3.draw(win)
    left4.setFill("red")
    text4 = Text(Point(50,260), "Counter")
    text4.draw(win)
    left5.setFill("red")
    text5 = Text(Point(50,320), "Grab")
    text5.draw(win)
    left6.setFill("red")
    text6 = Text(Point(50,380), "Taunt")
    text6.draw(win)
    right.setFill("green")
    text7 = Text(Point(740,80), "Strong")
    text7.draw(win)
    right2.setFill("green")
    text8 = Text(Point(740,140), "Light")
    text8.draw(win)
    right3.setFill("green")
    text9 = Text(Point(740,200), "Shield")
    text9.draw(win)
    right4.setFill("green")
    text10 = Text(Point(740,260), "Counter")
    text10.draw(win)
    right5.setFill("green")
    text11 = Text(Point(740,320), "Grab")
    text11.draw(win)
    right6.setFill("green")
    text12 = Text(Point(740,380), "Taunt")
    text12.draw(win)
    text = Text(Point(400, 583), "Exit")
    text.draw(win)

    quit.draw(win)

    return left, left2, left3, left4, left5, left6, right, right2, right3, right4, right5, right6, quit

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def playerpick(counter, stratlist, k, tauntboost, tauntboost2, trueblockability, trueblockability2,preset):
    if not(k == -1):
        k = len(stratlist)
    if k > counter and (stratlist[0] != ""):
        return stratlist[counter]
    return strategies(k, tauntboost, tauntboost2, trueblockability, trueblockability2,preset)

def strategies(k, tauntboost, tauntboost2, trueblockability, trueblockability2,preset):
    if k == -1:
        return genericpick2(preset)
    else:
        return genericpick(preset)
#1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48
def genericpick(preset =0):
    if preset == 0:
        r = random.choice([1,2,3,4,5,6])
    if preset == 1:
        r = random.choice([8,10,11])
        #r = random.choice([1,2,3,4,5,6])#variation like no taunt
    if preset == 2:
        r = random.choice([7,8,9,10,11,12])
    if preset == 3:
        r = random.choice([13,14,15,16,17,18])
    if preset == 4:
        r = random.choice([19,20,21,22,23,24])
    if preset == 5:
        r = random.choice([25,26,27,28,29,30])
    if preset == 6:
        r = random.choice([31,32,33,34,35,36])
    if preset == 7:
        r = random.choice([37,38,39,40,41,42])
    if preset == 8:
        r = random.choice([43,44,45,46,47,48])
    if r == 1:
        return "a1"
    if r == 2:
        return "a2"
    if r == 3:
        return "b1"
    if r == 4:
        return "b2"
    if r == 5:
        return "g"
    if r == 6:
        return "t"
    if r == 7:
        return "v1a1"
    if r == 8:
        return "v1a2"
    if r == 9:
        return "v1b1"
    if r == 10:
        return "v1b2"
    if r == 11:
        return "v1g"
    if r == 12:
        return "v1t"
    if r == 13:
        return "v2a1"
    if r == 14:
        return "v2a2"
    if r == 15:
        return "v2b1"
    if r == 16:
        return "v2b2"
    if r == 17:
        return "v2g"
    if r == 18:
        return "v2t"
    if r == 19:
        return "v3a1"
    if r == 20:
        return "v3a2"
    if r == 21:
        return "v3b1"
    if r == 22:
        return "v3b2"
    if r == 23:
        return "v3g"
    if r == 24:
        return "v3t"
    if r == 25:
        return "v4a1"
    if r == 26:
        return "v4a2"
    if r == 27:
        return "v4b1"
    if r == 28:
        return "v4b2"
    if r == 29:
        return "v4g"
    if r == 30:
        return "v4t"
    if r == 31:
        return "v5a1"
    if r == 32:
        return "v5a2"
    if r == 33:
        return "v5b1"
    if r == 34:
        return "v5b2"
    if r == 35:
        return "v5g"
    if r == 36:
        return "v5t"
    if r == 37:
        return "v6a1"
    if r == 38:
        return "v6a2"
    if r == 39:
        return "v6b1"
    if r == 40:
        return "v6b2"
    if r == 41:
        return "v6g"
    if r == 42:
        return "v6t"
    if r == 43:
        return "v7a1"
    if r == 44:
        return "v7a2"
    if r == 45:
        return "v7b1"
    if r == 46:
        return "v7b2"
    if r == 47:
        return "v7g"
    if r == 48:
        return "v7t"
    if r == 49:
        return "p"

def genericpick2(preset =0):
    r = random.choice([1,2,3,4,5,6])
    if preset == 1:
        r = random.choice([8,10,11])
        #r = random.choice([1,1,1,1,4,4,4,4,4,5,5,5,5])
    if preset == 2:
        r = random.choice([7,8,9,10,11,12])
    if preset == 3:
        r = random.choice([13,14,15,16,17,18])
    if preset == 4:
        r = random.choice([19,20,21,22,23,24])
    if preset == 5:
        r = random.choice([25,26,27,28,29,30])
    if preset == 6:
        r = random.choice([31,32,33,34,35,36])
    if preset == 7:
        r = random.choice([37,38,39,40,41,42])
    if preset == 8:
        r = random.choice([43,44,45,46,47,48])
    if r == 1:
        return "a1"
    if r == 2:
        return "a2"
    if r == 3:
        return "b1"
    if r == 4:
        return "b2"
    if r == 5:
        return "g"
    if r == 6:
        return "t"
    if r == 7:
        return "v1a1"
    if r == 8:
        return "v1a2"
    if r == 9:
        return "v1b1"
    if r == 10:
        return "v1b2"
    if r == 11:
        return "v1g"
    if r == 12:
        return "v1t"
    if r == 13:
        return "v2a1"
    if r == 14:
        return "v2a2"
    if r == 15:
        return "v2b1"
    if r == 16:
        return "v2b2"
    if r == 17:
        return "v2g"
    if r == 18:
        return "v2t"
    if r == 19:
        return "v3a1"
    if r == 20:
        return "v3a2"
    if r == 21:
        return "v3b1"
    if r == 22:
        return "v3b2"
    if r == 23:
        return "v3g"
    if r == 24:
        return "v3t"
    if r == 25:
        return "v4a1"
    if r == 26:
        return "v4a2"
    if r == 27:
        return "v4b1"
    if r == 28:
        return "v4b2"
    if r == 29:
        return "v4g"
    if r == 30:
        return "v4t"
    if r == 31:
        return "v5a1"
    if r == 32:
        return "v5a2"
    if r == 33:
        return "v5b1"
    if r == 34:
        return "v5b2"
    if r == 35:
        return "v5g"
    if r == 36:
        return "v5t"
    if r == 37:
        return "v6a1"
    if r == 38:
        return "v6a2"
    if r == 39:
        return "v6b1"
    if r == 40:
        return "v6b2"
    if r == 41:
        return "v6g"
    if r == 42:
        return "v6t"
    if r == 43:
        return "v7a1"
    if r == 44:
        return "v7a2"
    if r == 45:
        return "v7b1"
    if r == 46:
        return "v7b2"
    if r == 47:
        return "v7g"
    if r == 48:
        return "v7t"
    if r == 49:
        return "p"

def attributize(str):
    attackspeed = 9
    damage = 0
    attacktype = "error"
    lifeheal = 0
    attackmultiplier = 70
    countervalue = 0
    seedincrement = 0
    lifedrain = 0
    counterweakness = 1
    blockpenalty = 0
    blockbooster = 0
    blockability = 0
    tauntkiller = 1
    shieldnegate = 0
    remover = 0
    strongmultiplier = 1
    tauntincrement = 0
    tradeheal = 0
    healattribute = 1
    grabweakness = 1
    grabattribute = 1
    healconattribute = 0
    healcounter = 0
    hitlessheal = 0
    tauntvtauntdamage = 0
    armormultiplierattribute = 1
    armorgain = 0
    armorattack = 0
    counterbonus = 0
    tauntnegation = 0
    preventattribute = 1
    if str == "v7a1":
        attackspeed = 4
        damage = 9
        counterbonus = 3
        attacktype = "strong"
    if str == "v7a2":
        attackspeed = 2
        damage = 3
        attacktype = "light"#originally 2 damage but couldnt take damage from counter, too broken because couldnt be beaten
    if str == "v7b1":
        attackspeed = 2
        damage = 0
        tauntnegation = 1
        attacktype = "shield"
    if str == "v7b2":
        attackspeed = 2
        damage = 9
        strongmultiplier = (1/3)
        attacktype = "counter"
        countervalue = 0
    if str == "v7g":
        attackspeed = 2
        damage = 7
        tauntkiller = 0
        attacktype = "grab"
    if str == "v7t":
        attackspeed = 2
        damage = 0
        preventattribute = 0
        attacktype = "taunt"
    if str == "v6a1":
        attackspeed = 4
        damage = 6
        armorgain = 3 # originally 2
        attacktype = "strong"
    if str == "v6a2":
        attackspeed = 2
        damage = 2
        armorgain = 1
        attacktype = "light"
    if str == "v6b1":
        attackspeed = 2
        damage = 0
        armorgain = 3 #originally 0 and also only works against b1 and b2
        attacktype = "shield"
    if str == "v6b2":
        attackspeed = 2
        damage = 5 #originally 5
        armorgain = 1 #originally 5
        attacktype = "counter"
    if str == "v6mistakeb2":
        attackspeed = 2
        damage = 0
        armorattack = 1
        attacktype = "counter"
    if str == "v6g":
        attackspeed = 2
        damage = 2 # originally 0
        armorattack = 1
        attacktype = "grab"
    if str == "v6t":
        attackspeed = 2
        damage = 0
        armormultiplierattribute = 2
        attacktype = "taunt"
    if str == "v5a1":
        attackspeed = 3
        damage = 5 # originally 6
        attacktype = "strong"
    if str == "v5a2":
        attackspeed = 2
        damage = 4 # originally 5
        tauntkiller = 0
        lifeheal = -1
        attacktype = "light"
    if str == "v5b1":
        attackspeed = 2
        damage = 0
        lifeheal = 1
        hitlessheal = 2
        attacktype = "shield"
    if str == "v5b2":
        attackspeed = 2
        damage = 2 # originally 2
        strongmultiplier = (1/2) # originally 1
        grabattribute = 2
        attacktype = "counter"
    if str == "v5g":
        attackspeed = 2
        damage = 5 # originally 7
        attacktype = "grab"
    if str == "v5t":
        attackspeed = 2
        tauntvtauntdamage = 20
        attacktype = "taunt"
    if str == "v4a1":
        attackspeed = 4
        damage = 5
        lifeheal = 5
        tradeheal = 2
        attacktype = "strong"
    if str == "v4a2":
        attackspeed = 2
        damage = 2
        tauntkiller = 2
        healattribute = 3
        attacktype = "light"
    if str == "v4b1":
        attackspeed = 2
        damage = 0
        lifeheal = 3 # originally 4
        attacktype = "shield"
        grabweakness = 2
    if str == "v4b2":
        attackspeed = 2
        damage = 3 # originally 2
        healcounter = 1
        attacktype = "counter"
    if str == "v4g":
        attackspeed = 2
        damage = 7
        lifedrain = -1
        attacktype = "grab"
    if str == "v4t":
        attackspeed = 2
        damage = 0
        attacktype = "taunt"
        healconattribute = 1
    if str == "v3a1":
        attackspeed = 4
        damage = 7
        tauntkiller = 2
        attacktype = "strong"
    if str == "v3a2":
        attackspeed = 2
        damage = 2#originally 1
        shieldnegate = 1
        attacktype = "light"
    if str == "v3b1":
        attackspeed = 2
        damage = 0
        remover = 1
        attacktype = "shield"
    if str == "v3b2":
        attackspeed = 2
        damage = 2
        strongmultiplier = 6
        attacktype = "counter"
        countervalue = 0
    if str == "v3g":
        attackspeed = 1
        damage = 4
        attacktype = "grab"
    if str == "v3t":
        attackspeed = 2
        damage = 0
        attacktype = "taunt"
        tauntincrement = 1
    if str == "v2a1":
        attackspeed = 4
        damage = 10
        blockpenalty = 1
        attacktype = "strong"
    if str == "v2a2":
        attackspeed = 3
        damage = 4
        attacktype = "light"
    if str == "v2b1":
        attackspeed = 2
        damage = 0
        blockbooster = 2
        attacktype = "shield"
    if str == "v2b2":
        attackspeed = 2
        damage = 0
        attacktype = "counter"
        countervalue = 0
        lifedrain = 3
    if str == "v2g":
        attackspeed = 2
        damage = 0
        lifedrain = 4 # originally 3
        attacktype = "grab"
    if str == "v2t":
        attackspeed = 2
        damage = 0
        attacktype = "taunt"
        blockability = 1
        lifedrain = 0
    if str == "v1a1":
        attackspeed = 4
        damage = 6
        lifedrain = 1 # originally 2
        seedincrement = 1
        attacktype = "strong"
    if str == "v1a2":
        attackspeed = 2
        damage = 5#originally 5
        counterweakness = 2
        attacktype = "light"
    if str == "v1b1":
        attackspeed = 2
        damage = 0
        attacktype = "shield"
        seedincrement = 2
    if str == "v1b2":
        attackspeed = 2
        damage = 6
        attacktype = "counter"
        countervalue = 0
    if str == "v1g":
        attackspeed = 2
        damage = 4
        attacktype = "grab"
        seedincrement = 3
    if str == "v1t":
        attackspeed = 2
        damage = 0
        attacktype = "taunt"
        seedincrement = 5
    if str == "p":
        attackspeed = 5
        damage = 0
        attacktype = "pass"
    if str == "t":
        attackspeed = 2
        damage = 0
        attacktype = "taunt"
        attackmultiplier = 2
    if str == "a1":
        attackspeed = 4
        damage = 8
        attacktype = "strong"
    if str == "a2":
        attackspeed = 2
        damage = 3
        attacktype = "light"
    if str == "b1":
        attackspeed = 2
        damage = 0
        lifeheal = 2
        attacktype = "shield"
    if str == "b2":
        attackspeed = 2
        damage = 0
        countervalue = 1
        attacktype = "counter"
    if str == "g":
        attackspeed = 2
        damage = 6
        attacktype = "grab"
    return attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healattribute, grabweakness, grabattribute, healconattribute, healcounter, hitlessheal, tauntvtauntdamage, armormultiplierattribute, armorgain, armorattack, counterbonus, tauntnegation, preventattribute

def battle(attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, seedcount, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockboost, blockability, trueblockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healmultiplier, healattribute, grabweakness, grabattribute, healconattribute, healcounter, attacktype2, attackspeed2, damage2, attackmultiplier2, lifeheal2, countervalue2, seedcount2, lifedrain2, counterweakness2, seedincrement2, blockpenalty2, blockbooster2, blockboost2, blockability2, trueblockability2, tauntkiller2, shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healmultiplier2, healattribute2, grabweakness2, grabattribute2, healconattribute2, healcounter2, p1health, p2health, tauntboost, tauntboost2, tracker, gametracker, removera1, removera2, removera12, removera22, tauntvalue, tauntvalue2, grabmultiplier, grabmultiplier2, healcon, healcon2, hitlessheal, hitlessheal2, tauntvtauntdamage, tauntvtauntdamage2, armormultiplier, armormultiplier2, armorgain, armorgain2, armor, armor2, armorattack, armorattack2, armormultiplierattribute, armormultiplierattribute2, counterbonus, counterbonus2, tauntnegation, tauntnegation2, preventattribute, preventattribute2, prevent, prevent2):
    # value that shows wasted turn
    wasted = 0
    #trackervalue start, comment either this or at the end depending on if you want to test before or after turn of successs
    """
    if gametracker == 0 and tauntvalue2 == 3:
        tracker = tracker + 1
        gametracker = 1
    #trackervalue end
    """
    seedboost = 1
    seedboost2 = 1
    seedmax = 12
        #beginning of logic
    #if seedcount > (seedmax-3) and attacktype == "taunt" and seedincrement > 2:
        #wasted = 1
        #return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
    #if seedcount2 > (seedmax-3) and attacktype2 == "taunt" and seedincrement2 > 2:
        #wasted = 1
        #return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
        #ending of logic
    #beginning of seed health values
    a = seedcount
    b = seedcount2
    #end of seed health values
    if seedcount > (seedmax-1):
        seedboost = 2
    if seedcount2 > (seedmax-1):
        seedboost2 = 2
    if attacktype == "pass":
        if attacktype2 == "pass":
            pass
        if attacktype2 == "taunt":
            if attackmultiplier2 == 2:
                tauntboost2 = 2
            seedcount2 = seedcount2 + seedincrement2
            if trueblockability2 == 0 and blockability2 == 1:
                trueblockability2 = 1
            tauntvalue2 = tauntvalue2 + tauntincrement2
            if tauntvalue2 == 1 and tauntincrement2 == 1:
                p2health = p2health - 2 * prevent2
                prevent2 = 1
            if tauntvalue2 == 2 and tauntincrement2 == 1:
                p2health = p2health + 2
            if tauntvalue2 == 3 and tauntincrement2 == 1:
                p1health = p1health - 25 * prevent
                prevent = 1
            if healconattribute2 == 1:
                healcon2 = healconattribute2
            p2health = p2health + lifedrain2
            p1health = p1health - lifedrain2 * prevent
            if lifedrain2 > 0 and prevent == 0:
                prevent = 1
            if armormultiplierattribute2 == 2:
                armormultiplier2 = 2
            if preventattribute2 == 0:
                prevent2 = 0
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                    healmultiplier2 = 1
                    prevent = 1
                    healcon2 = 0
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 > 0:
                    healmultiplier2 = 1
            tauntboost2 = 1
            seedcount2 = seedcount2 + seedincrement2
            trueblockability2 = 0
            blockboost2 = 0
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if damage2 > 0:
                p1health = p1health-(damage2 + blockboost2)*tauntboost2*seedboost2*prevent
                prevent = 1
                tauntboost2 = 1
                trueblockability2 = 0
                blockboost2 = 0
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 != 0:
                    healmultiplier2 = 1
        if attacktype2 == "shield":
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - (lifeheal2 + hitlessheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                    healmultiplier = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + (lifeheal2 + hitlessheal2) * healmultiplier2
                if lifeheal2 + hitlessheal2 > 0:
                    healmultiplier2 = 1
            seedcount2 = seedcount2 + seedincrement2
            blockboost2 = blockboost2 + blockbooster2
        if attacktype2 == "counter":
            if grabattribute2 == 2:
                grabmultiplier2 = grabattribute2
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
        if attacktype2 == "grab":
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * prevent
                prevent = 1
            if armorattack2 > 0:
                p1health = p1health - (armor2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * prevent
                prevent = 1
                armor2 = 0
            if damage2 > 0 or armorattack2 > 0:
                tauntboost2 = 1
                blockboost2 = 0
                grabmultiplier2 = 1
            seedcount2 = seedcount2 + seedincrement2
            if lifedrain2 > 0 and prevent == 0:
                prevent = 1
            p1health = p1health - lifedrain2 * prevent
            p2health = p2health + lifedrain2
    if attacktype == "taunt":
        if attacktype2 == "pass":
            if attackmultiplier == 2:
                tauntboost = 2
            seedcount = seedcount + seedincrement
            if trueblockability == 0 and blockability == 1:
                trueblockability = 1
            tauntvalue = tauntvalue + tauntincrement
            if tauntvalue == 1 and tauntincrement == 1:
                p1health = p1health - 2 * prevent
                prevent = 1
            if tauntvalue == 2 and tauntincrement == 1:
                p1health = p1health + 2
            if tauntvalue == 3 and tauntincrement == 1:
                p2health = p2health - 25 * prevent2
                prevent2 = 1
            if healconattribute == 1:
                healcon = healconattribute
            if lifedrain > 0 and prevent2 == 0:
                prevent2 = 1
            p1health = p1health + lifedrain
            p2health = p2health - lifedrain * prevent2 #technically I need to combine prevent2's but there's no move with tauntcounter and lifedrain
            if armormultiplierattribute == 2:
                armormultiplier = 2
            if preventattribute == 0:
                prevent = 0
        if attacktype2 == "taunt":
            if attackmultiplier2 == 2:
                tauntboost2 = 2
            if attackmultiplier == 2:
                tauntboost = 2
            if preventattribute2 == 0:
                prevent2 = 0
            if preventattribute == 0:
                prevent = 0
            seedcount = seedcount + seedincrement
            seedcount2 = seedcount2 + seedincrement2
            if trueblockability == 0 and blockability == 1:
                trueblockability = 1
            if trueblockability2 == 0 and blockability2 == 1:
                trueblockability2 = 1
            tauntvalue = tauntvalue + tauntincrement
            tauntvalue2 = tauntvalue2 + tauntincrement2
            if tauntvalue2 == 1 and tauntincrement2 == 1:
                p2health = p2health - 2 * prevent2
                prevent2 = 1
            if tauntvalue2 == 3 and tauntincrement2 == 1:
                p1health = p1health - 25 * prevent
                prevent = 1
            if tauntvalue == 1 and tauntincrement == 1:
                p1health = p1health - 2 * prevent
                prevent = 1
            if tauntvalue == 3 and tauntincrement == 1:
                p2health = p2health - 25 * prevent2
                prevent2 = 1
            if tauntvalue2 == 2 and tauntincrement2 == 1:
                p2health = p2health + 2
            if tauntvalue == 2 and tauntincrement == 1:
                p1health = p1health + 2
            if healconattribute2 == 1:
                healcon2 = healconattribute2
            if healconattribute == 1:
                healcon = healconattribute
            p1health = p1health + lifedrain
            p2health = p2health - lifedrain * prevent2
            if lifedrain > 0 and prevent2 == 0:
                prevent2 = 1
            p2health = p2health + lifedrain2
            p1health = p1health - lifedrain2 * prevent
            if lifedrain2 > 0 and prevent == 0:
                prevent = 1
            p2health = p2health - tauntvtauntdamage * prevent2
            if tauntvtauntdamage > 0 and prevent2 == 0:
                prevent2 = 1
            p1health = p1health - tauntvtauntdamage2 * prevent
            if tauntvtauntdamage2 > 0 and prevent == 0:
                prevent = 1
            if armormultiplierattribute == 2:
                armormultiplier = 2
            if armormultiplierattribute2 == 2:
                armormultiplier2 = 2
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * tauntkiller2 * seedboost2 * prevent
                prevent = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 > 0:
                    healmultiplier2 = 1
            tauntboost2 = 1
            seedcount2 = seedcount2 + seedincrement2
            trueblockability2 = 0
            if tauntkiller2 > 0:
                blockboost2 = 0
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if damage2 > 0:
                p1health = p1health - ((damage2 + blockboost2) * tauntboost2 * seedboost2 * tauntkiller2) * prevent
                prevent = 1
                tauntboost2 = 1
                trueblockability2 = 0
                blockboost2 = 0
            if healattribute2 > 1:
                healmultiplier2 = healattribute2
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 != 0:
                    healmultiplier2 = 1
        if attacktype2 == "shield":
            if tauntnegation2 != 1:
                if attackmultiplier == 2:
                    tauntboost = 2
                seedcount = seedcount + seedincrement
                if trueblockability == 0 and blockability == 1:
                    trueblockability = 1
                tauntvalue = tauntvalue + tauntincrement
                if tauntvalue == 1 and tauntincrement == 1:
                    p1health = p1health - 2 * prevent
                    prevent = 1
                if tauntvalue == 2 and tauntincrement == 1:
                    p1health = p1health + 2
                if tauntvalue == 3 and tauntincrement == 1:
                    p2health = p2health - 25 * prevent2
                    prevent2 = 1
                if healconattribute == 1:
                    healcon = healconattribute
                p1health = p1health + lifedrain
                p2health = p2health - lifedrain * prevent2
                if lifedrain > 0:
                    prevent2 = 1
                if armormultiplierattribute == 2:
                    armormultiplier = 2
                if preventattribute == 0:
                    prevent = 0
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + hitlessheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + (lifeheal2 + hitlessheal2) * healmultiplier2
                if lifeheal2 + hitlessheal2 > 0:
                    healmultiplier2 = 1
            seedcount2 = seedcount2 + seedincrement2
            blockboost2 = blockboost2 + blockbooster2
            armor2 = armor2 + armorgain2 * armormultiplier2
            if armorgain2 > 0:
                armormultiplier2 = 1
        if attacktype2 == "counter":
            if attackmultiplier == 2:
                tauntboost = 2
            seedcount = seedcount + seedincrement
            if trueblockability == 0 and blockability == 1:
                trueblockability = 1
            tauntvalue = tauntvalue + tauntincrement
            if tauntvalue == 1 and tauntincrement == 1:
                p1health = p1health - 2 * prevent
                prevent = 1
            if tauntvalue == 2 and tauntincrement == 1:
                p1health = p1health + 2
            if tauntvalue == 3 and tauntincrement == 1:
                p2health = p2health - 25 * prevent2
                prevent2 = 1
            if grabattribute2 == 2:
                grabmultiplier2 = grabattribute2
            if healconattribute == 1:
                healcon = healconattribute
            if preventattribute == 0:
                prevent = 0
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if armormultiplierattribute == 2:
                armormultiplier = 2
        if attacktype2 == "grab":
            if damage2 > 0:
                p1health = p1health - ((damage2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * tauntkiller2) * prevent
            if armorattack2 > 0:
                p1health = p1health - (armor2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * tauntkiller2 * prevent
                armor2 = 0
            if damage2 > 0 or armorattack2 > 0:
                tauntboost2 = 1
                blockboost2 = 0
                prevent = 1
                grabmultiplier2 = 1
            seedcount2 = seedcount2 + seedincrement2
            p1health = p1health - lifedrain2 * prevent
            if lifedrain2 > 0:
                prevent = 1
            p2health = p2health + lifedrain2
    if attacktype == "strong":
        if removera1 == 1:
            wasted = 1
            return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
        if attacktype2 == "pass":
            if damage > 0:
                p2health = p2health -(damage + blockboost)*tauntboost * seedboost * prevent2
                prevent2 = 1
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
            else:
                p1health = p1health + lifeheal * healmultiplier
                if lifeheal > 0:
                    healmultiplier = 1
            tauntboost = 1
            trueblockability = 0
            seedcount = seedcount + seedincrement
            blockboost = 0
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
        if attacktype2 == "taunt":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * tauntkiller * seedboost * prevent2
                prevent2 = 1
            seedcount = seedcount + seedincrement
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
            else:
                p1health = p1health + lifeheal * healmultiplier
                if lifeheal > 0:
                    healmultiplier = 1
            tauntboost = 1
            trueblockability = 0
            if tauntkiller > 0:
                blockboost = 0
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if attackspeed < attackspeed2:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * tauntkiller * seedboost * prevent2
                    prevent2 = 1
                seedcount = seedcount + seedincrement
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                else:
                    p1health = p1health + lifeheal * healmultiplier
                    if lifeheal > 0:
                        healmultiplier = 1
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
            elif attackspeed > attackspeed2:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * tauntkiller2 * seedboost2 * prevent
                    prevent = 1
                seedcount2 = seedcount2 + seedincrement2
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                        healmultiplier2 = 1
                        prevent = 1
                        healcon2 = 0
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 > 0:
                        healmultiplier2 = 1
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
            else:
                if healcon == 1:
                    if tradeheal > 0:
                        p2health = p2health- (tradeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                        blockboost = 0
                else:
                    p1health = p1health + tradeheal * healmultiplier
                    if tradeheal > 0:
                        healmultiplier = 1
                if healcon2 == 1:
                    if tradeheal2 > 0:
                        p1health = p1health - (tradeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                        healmultiplier2 = 1
                        prevent = 1
                        healcon2 = 0
                        blockboost2 = 0
                else:
                    p2health = p2health + tradeheal2 * healmultiplier2
                    if tradeheal2 > 0:
                        healmultiplier2 = 1
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
            tauntboost = 1
            tauntboost2 = 1
            trueblockability = 0
            trueblockability2 = 0
            blockboost = 0
            blockboost2 = 0
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            tauntboost = 1
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                prevent = 1
            tauntboost2 = 1
            trueblockability = 0
            trueblockability2 = 0
            blockboost2 = 0
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 != 0:
                    healmultiplier2 = 1
        if attacktype2 == "shield":
            if trueblockability == 1:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                    prevent2 = 1
                seedcount = seedcount + seedincrement
                k = healcon
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                else:
                    p1health = p1health + lifeheal * healmultiplier
                    if lifeheal > 0:
                        healmultiplier = 1
                tauntboost = 1
                trueblockability = 0
                blockboost = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
            else:
                if remover2 == 1:
                    removera1 = 1
                tauntboost = 1
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                        healmultiplier2 = 1
                        prevent = 1
                        healcon2 = 0
                        blockboost2 = 0
                        tauntboost2 = 1
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 > 0:
                        healmultiplier2 = 1
                p1health = p1health - (lifedrain2 + blockpenalty) * prevent
                if lifedrain2 + blockpenalty > 0:
                    prevent = 1
                p2health = p2health + lifedrain2
                seedcount2 = seedcount2 + seedincrement2
                blockboost2 = blockboost2 + blockbooster2
                armor2 = armor2 + armorgain2 * armormultiplier2
                if armorgain2 > 0:
                    armormultiplier2 = 1
        if attacktype2 == "counter":
            if trueblockability == 1:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                    prevent2 = 1
                seedcount = seedcount + seedincrement
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                else:
                    p1health = p1health + lifeheal * healmultiplier
                    if lifeheal > 0:
                        healmultiplier = 1
                tauntboost = 1
                trueblockability = 0
                blockboost = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
            else:
                if countervalue2 > 0:
                    if damage > 0:
                        p1health = p1health-((((damage + blockboost)*tauntboost*countervalue2) * strongmultiplier2 * seedboost) + counterbonus) * prevent
                        prevent = 1
                        blockboost = 0
                        counterbonus = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
                if damage2 > 0:
                    p1health = p1health - (((damage2 + blockboost2) * tauntboost2 * strongmultiplier2 * seedboost2) + counterbonus) * prevent
                    prevent = 1
                    counterbonus = 0
                if armorattack2 > 0:
                    p1health = p1health - (((armor2 + blockboost2) * tauntboost2 * strongmultiplier2 * seedboost2) + counterbonus) * prevent
                    prevent = 1
                    armor2 = 0
                if damage2 > 0 or armorattack2 > 0:
                    tauntboost2 = 1
                    blockboost2 = 0
                if grabattribute2 == 2:
                    grabmultiplier2 = grabattribute2
                p1health = p1health - lifedrain2 * prevent
                if lifedrain2 > 0:
                    prevent = 1
                p2health = p2health + lifedrain2
                if not(healcon == 1):
                    p2health = p2health + (damage + blockboost) * healmultiplier2 * tauntboost * seedboost * healcounter2
                    if healcounter2 > 0:
                        blockboost = 0
                        healmultiplier2 = 1
                else:
                    if damage > 0:
                        if healcounter > 0:
                            p1health = p1health - (damage + blockboost) * tauntboost * seedboost * healmultiplier2 * healcounter2 * prevent
                            healcon = 0
                            if healcounter2 > 0:
                                blockboost = 0
                                healmultiplier2 = 1
                                prevent = 1
                tauntboost = 1
                blockboost = 0
        if attacktype2 == "grab":
            if damage > 0:
                p2health = p2health - (damage + blockboost) *tauntboost * seedboost * prevent2
                prevent2 = 1
            k = healcon
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + blockboost + lifedrain) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
            else:
                p1health = p1health + (lifeheal+ lifedrain) * healmultiplier
                p2health = p2health - lifedrain * healmultiplier
                if lifeheal > 0:
                    healmultiplier = 1
            tauntboost = 1
            seedcount = seedcount + seedincrement
            trueblockability = 0
            blockboost = 0
            tauntboost2 = 1
            grabmultiplier2 = 1
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
    if attacktype == "light":
        if removera2 == 1:
            wasted = 1
            return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
        if attacktype2 == "pass":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                prevent2 = 1
                tauntboost = 1
                trueblockability = 0
                blockboost = 0
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal != 0:
                    healmultiplier = 1
        if attacktype2 == "taunt":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * seedboost * tauntkiller * prevent2
                prevent2 = 1
                tauntboost = 1
                trueblockability = 0
                blockboost = 0
            if healattribute > 1:
                healmultiplier = healattribute
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal != 0:
                    healmultiplier = 1
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            tauntboost2 = 1
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                prevent2 = 1
                tauntboost = 1
                trueblockability = 0
                trueblockability2 = 0
                blockboost = 0
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal != 0:
                    healmultiplier = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if attackspeed > attackspeed2:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                    blockboost2 = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - ((
                                               lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                        healmultiplier2 = 1
                        healcon2 = 0
                        blockboost2 = 0
                        prevent = 1
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 != 0:
                        healmultiplier2 = 1
            if attackspeed2 > attackspeed:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                    prevent2 = 1
                blockboost = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (
                                              lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                        blockboost = 0
                else:
                    p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                    if lifeheal + hitlessheal != 0:
                        healmultiplier = 1
            else:
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
            tauntboost2 = 1
            tauntboost = 1
            trueblockability = 0
            trueblockability2 = 0
        if attacktype2 == "shield":
            if trueblockability == 1:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                    tauntboost = 1
                    prevent2 = 1
                    trueblockability = 0
                    blockboost = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (
                                              lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                        blockboost = 0
                else:
                    p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                    if lifeheal + hitlessheal != 0:
                        healmultiplier = 1
            else:
                if shieldnegate == 1:
                    tauntboost = 1
                else:
                    if remover2 == 1:
                        removera2 = 1
                    tauntboost = 1
                    if healcon2 == 1:
                        if lifeheal2 > 0:
                            p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                            healmultiplier2 = 1
                            prevent = 1
                            healcon2 = 0
                            blockboost2 = 0
                    else:
                        p2health = p2health + lifeheal2 * healmultiplier2
                        if lifeheal2 > 0:
                            healmultiplier2 = 1
                    p1health = p1health - (lifedrain2 + blockpenalty) * prevent
                    if lifedrain2 + blockpenalty > 0:
                        prevent = 1
                    p2health = p2health + lifedrain2
                    seedcount2 = seedcount2 + seedincrement2
                    blockboost2 = blockboost2 + blockbooster2
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    if armorgain2 > 0:
                        armormultiplier2 = 1
        if attacktype2 == "counter":
            if trueblockability == 1:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                    prevent2 = 1
                tauntboost = 1
                seedcount = seedcount + seedincrement
                trueblockability = 0
                blockboost = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (
                                              lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                        blockboost = 0
                else:
                    p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                    if lifeheal + hitlessheal != 0:
                        healmultiplier = 1
            else:
                if countervalue2 > 0:
                    if damage > 0:
                        p1health = p1health - ((damage + blockboost) * tauntboost * countervalue2 * counterweakness * seedboost) * prevent
                        prevent = 1
                        blockboost = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                if armorattack2 > 0:
                    p1health = p1health - (armor2 + blockboost2) * tauntboost2* seedboost2 * prevent
                    prevent = 1
                    armor2 = 0
                if damage2 > 0 or armorattack2 > 0:
                    tauntboost2 = 1
                    blockboost2 = 0
                if grabattribute2 == 2:
                    grabmultiplier2 = grabattribute2
                p1health = p1health - lifedrain2 * prevent
                if lifedrain2 > 0:
                    prevent = 1
                p2health = p2health + lifedrain2
                if not(healcon2 == 1):
                    p2health = p2health + (damage + blockboost) * healmultiplier2 * tauntboost * seedboost * healcounter2
                    if healcounter2 > 0:
                        blockboost = 0
                        healmultiplier2 = 1
                else:
                    if healcounter2 > 0:
                        if damage > 0:
                            p1health = p1health - (damage + blockboost) * tauntboost * seedboost * healmultiplier2 * healcounter2 * counterweakness * prevent
                            prevent = 1
                            healmultiplier2 = 1
                            healcon2 = 0
                            blockboost = 0
                tauntboost = 1
        if attacktype2 == "grab":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                prevent2 = 1
                tauntboost = 1
                trueblockability = 0
                blockboost = 0
                grabmultiplier2 = 1
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal != 0:
                    healmultiplier = 1
            tauntboost2 = 1
    if attacktype == "shield":
        if attacktype2 == "pass":
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal > 0:
                    healmultiplier = 1
            seedcount = seedcount + seedincrement
            blockboost = blockboost + blockbooster
            armor = armor + armorgain * armormultiplier
            if armorgain > 0:
                armormultiplier = 1
        if attacktype2 == "taunt":
            if tauntnegation != 1:
                if attackmultiplier2 == 2:
                    tauntboost2 = 2
                seedcount2 = seedcount2 + seedincrement2
                if trueblockability2 == 0 and blockability2 == 1:
                    trueblockability2 = 1
                tauntvalue2 = tauntvalue2 + tauntincrement2
                if tauntvalue2 == 1 and tauntincrement2 == 1:
                    p2health = p2health - 2 * prevent2
                    prevent2 = 1
                if tauntvalue2 == 2 and tauntincrement2 == 1:
                    p2health = p2health + 2
                if tauntvalue2 == 3 and tauntincrement2 == 1:
                    p1health = p1health - 25 * prevent
                    prevent = 1
                if healconattribute2 == 1:
                    healcon2 = healconattribute2
                p2health = p2health + lifedrain2
                p1health = p1health - lifedrain2 * prevent
                if lifedrain2 > 0:
                    prevent = 1
                if armormultiplierattribute2 == 2:
                    armormultiplier2 = 2
                if preventattribute2 == 0:
                    prevent2 = 0
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal > 0:
                    healmultiplier = 1
            seedcount = seedcount + seedincrement
            blockboost = blockboost + blockbooster
            armor = armor + armorgain * armormultiplier
            if armorgain > 0:
                armormultiplier = 1
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if trueblockability2 == 1:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                seedcount2 = seedcount2 + seedincrement2
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                        healmultiplier2 = 1
                        prevent = 1
                        healcon2 = 0
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 > 0:
                        healmultiplier2 = 1
                tauntboost2 = 1
                trueblockability2 = 0
                blockboost2 = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
            else:
                if remover == 1:
                    removera12 = 1
                tauntboost2 = 1
                if healcon == 1:
                    if lifeheal > 0:
                        p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                        healmultiplier = 1
                        prevent2 = 1
                        healcon = 0
                        blockboost = 0
                else:
                    p1health = p1health + lifeheal * healmultiplier
                    if lifeheal > 0:
                        healmultiplier = 1
                p2health = p2health - (lifedrain + blockpenalty2) * prevent2
                if lifedrain + blockpenalty2 > 0:
                    prevent2 = 1
                p1health = p1health + lifedrain
                seedcount = seedcount + seedincrement
                blockboost = blockboost + blockbooster
                armor = armor + armorgain * armormultiplier
                if armorgain > 0:
                    armormultiplier = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if trueblockability2 == 1:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                    tauntboost2 = 1
                    blockboost2 = 0
                    trueblockability2 = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - ((
                                               lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                        healmultiplier2 = 1
                        healcon2 = 0
                        blockboost2 = 0
                        prevent = 1
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 != 0:
                        healmultiplier2 = 1
            else:
                if shieldnegate2 == 1:
                    tauntboost2 = 1
                else:
                    if remover == 1:
                        removera22 = 1
                    tauntboost2 = 1
                    if healcon == 1:
                        if lifeheal > 0:
                            p2health = p2health - (lifeheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                            healmultiplier = 1
                            prevent2 = 1
                            blockboost = 0
                            healcon = 0
                    else:
                        p1health = p1health + lifeheal * healmultiplier
                        if lifeheal > 0:
                            healmultiplier = 1
                    p2health = p2health - (lifedrain + blockpenalty2) * prevent2
                    if lifedrain + blockpenalty2 > 0:
                        prevent2 = 1
                    p1health = p1health + lifedrain
                    seedcount = seedcount + seedincrement
                    blockboost = blockboost + blockbooster
                    armor = armor + armorgain * armormultiplier
                    if armorgain > 0:
                        armormultiplier = 1
        if attacktype2 == "shield":
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal > 0:
                    healmultiplier = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - (lifeheal2 + hitlessheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                    healmultiplier2 = 1
                    prevent = 1
                    healcon2 = 0
                    blockboost2 = 0
            else:
                p2health = p2health + (lifeheal2 + hitlessheal2) * healmultiplier2
                if lifeheal2 + hitlessheal2 > 0:
                    healmultiplier2 = 1
            seedcount = seedcount + seedincrement
            seedcount2 = seedcount2 + seedincrement2
            blockboost2 = blockboost2 + blockbooster2
            blockboost = blockboost + blockbooster
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
        if attacktype2 == "counter":
            if healcon == 1:
                if lifeheal > 0:
                    p2health = p2health - (lifeheal + hitlessheal + blockboost) * healmultiplier * tauntboost * seedboost * prevent2
                    healmultiplier = 1
                    prevent2 = 1
                    healcon = 0
                    blockboost = 0
            else:
                p1health = p1health + (lifeheal + hitlessheal) * healmultiplier
                if lifeheal + hitlessheal > 0:
                    healmultiplier = 1
            seedcount = seedcount + seedincrement
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            blockboost = blockboost + blockbooster
            if grabattribute2 == 2:
                grabmultiplier2 = grabattribute2
        if attacktype2 == "grab":
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * grabweakness * prevent
            if armorattack2 > 0:
                p1health = p1health - (armor2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * grabweakness * prevent
                armor2 = 0
            if damage2 > 0 or armorattack2 > 0:
                tauntboost2 = 1
                prevent = 1
                blockboost2 = 0
                grabmultiplier2 = 1
            p1health = p1health - lifedrain2 * prevent
            if lifedrain2 > 0:
                prevent = 1
            p2health = p2health + lifedrain2
            seedcount2 = seedcount2 + seedincrement2

    if attacktype == "counter":
        if attacktype2 == "pass":
            if grabattribute == 2:
                grabmultiplier = grabattribute
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
        if attacktype2 == "taunt":
            if attackmultiplier2 == 2:
                tauntboost2 = 2
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            seedcount2 = seedcount2 + seedincrement2
            if trueblockability2 == 0 and blockability2 == 1:
                trueblockability2 = 1
            tauntvalue2 = tauntvalue2 + tauntincrement2
            if tauntvalue2 == 1 and tauntincrement2 == 1:
                p2health = p2health - 2 * prevent2
                prevent2 = 1
            if tauntvalue2 == 2 and tauntincrement2 == 1:
                p2health = p2health + 2
            if tauntvalue2 == 3 and tauntincrement2 == 1:
                p1health = p1health - 25 * prevent
                prevent = 1
            if grabattribute == 2:
                grabmultiplier = grabattribute
            if healconattribute2 == 1:
                healcon2 = healconattribute2
            if preventattribute2 == 0:
                prevent2 = 0
            if armormultiplierattribute2 == 2:
                armormultiplier2 = 2
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if trueblockability2 == 1:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                seedcount2 = seedcount2 + seedincrement2
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - (lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                        healmultiplier = 1
                        prevent = 1
                        healcon2 = 0
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 > 0:
                        healmultiplier2 = 1
                trueblockability2 = 0
                tauntboost2 = 1
                blockboost2 = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
            else:
                if countervalue > 0:
                    if damage2 > 0:
                        p2health = p2health - ((((damage2 + blockboost2) * tauntboost2 * countervalue)* strongmultiplier * seedboost2) + counterbonus2) * prevent2
                        prevent2 = 1
                        counterbonus2 = 0
                        blockboost2 = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if damage > 0:
                    p2health = p2health - (((damage + blockboost) * tauntboost * strongmultiplier * seedboost) + counterbonus2) * prevent2
                    prevent2 = 1
                    counterbonus2 = 0
                if armorattack > 0:
                    p2health = p2health - (((armor + blockboost) * tauntboost * strongmultiplier * seedboost) + counterbonus2) * prevent
                    prevent = 1
                    armor = 0
                if damage > 0 or armorattack > 0:
                    tauntboost = 1
                    blockboost = 0
                if grabattribute == 2:
                    grabmultiplier = grabattribute
                p2health = p2health - lifedrain * prevent2
                if lifedrain > 0:
                    prevent2 = 1
                p1health = p1health + lifedrain
                if not(healcon2 == 1):
                    p1health = p1health + (damage2 + blockboost2) * healmultiplier * tauntboost2 * seedboost2 * healcounter
                    if healcounter > 0:
                        healmultiplier = 1
                        blockboost2 = 0
                else:
                    if healcounter2 > 0:
                        if damage2 > 0:
                            p2health = p2health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * healmultiplier * healcounter * prevent2
                            prevent2 = 1
                            healcon2 = 0
                            if healcounter > 0:
                                blockboost2 = 0
                                healmultiplier = 1
                blockboost2 = 0
                tauntboost2 = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if trueblockability2 == 1:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                    prevent = 1
                    tauntboost2 = 1
                    seedcount2 = seedcount2 + seedincrement2
                    trueblockability2 = 0
                    blockboost2 = 0
                if armorgain2 > 0:
                    armor2 = armor2 + armorgain2 * armormultiplier2
                    armormultiplier2 = 1
                if healcon2 == 1:
                    if lifeheal2 > 0:
                        p1health = p1health - ((
                                               lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                        healmultiplier2 = 1
                        healcon2 = 0
                        blockboost2 = 0
                        prevent = 1
                else:
                    p2health = p2health + lifeheal2 * healmultiplier2
                    if lifeheal2 != 0:
                        healmultiplier2 = 1
            else:
                if countervalue > 0:
                    if damage2 > 0:
                        p2health = p2health - ((damage2 + blockboost2) * tauntboost2 * countervalue * counterweakness2) * seedboost2 * prevent2
                        prevent2 = 1
                        blockboost2 = 0
                if armorgain > 0:
                    armor = armor + armorgain * armormultiplier
                    armormultiplier = 1
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * seedboost * prevent2
                if armorattack > 0:
                    p2health = p2health - (armor + blockboost) * tauntboost * seedboost * prevent2
                    armor = 0
                if damage > 0 or armorattack > 0:
                    tauntboost = 1
                    prevent2 = 1
                    blockboost = 0
                if grabattribute == 2:
                    grabmultiplier = grabattribute
                p2health = p2health - lifedrain * prevent2
                if lifedrain > 0:
                    prevent2 = 1
                p1health = p1health + lifedrain
                if not(healcon == 1):
                    p1health = p1health + (damage2 + blockboost2) * healmultiplier * tauntboost2 * seedboost2 * healcounter
                    if healcounter > 0:
                        blockboost2 = 0
                        healmultiplier = 1
                else:
                    if healcounter > 0:
                        if damage2 > 0:
                            p2health = p2health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * healmultiplier * healcounter * counterweakness2 * prevent2
                            healmultiplier = 1
                            prevent2 = 1
                            healcon = 0
                            blockboost2 = 0
                tauntboost2 = 1
        if attacktype2 == "shield":
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - (lifeheal2 + hitlessheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                    healmultiplier2 = 1
                    prevent = 1
                    healcon2 = 0
                    blockboost2 = 0
            else:
                p2health = p2health + (lifeheal2 + hitlessheal2) * healmultiplier2
                if lifeheal2 + hitlessheal2 > 0:
                    healmultiplier2 = 1
            seedcount2 = seedcount2 + seedincrement2
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            blockboost2 = blockboost2 + blockbooster2
            if grabattribute == 2:
                grabmultiplier = grabattribute
        if attacktype2 == "counter":
            if grabattribute == 2:
                grabmultiplier = grabattribute
            if grabattribute2 == 2:
                grabmultiplier2 = grabattribute2
            if armorgain > 0:
                armor = armor + armorgain * armormultiplier
                armormultiplier = 1
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
        if attacktype2 == "grab":
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * prevent
            if armorattack2 > 0:
                p1health = p1health - (armor2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * prevent
                armor2 = 0
            if damage2 > 0 or armorattack2 > 0:
                tauntboost2 = 1
                prevent = 1
                blockboost2 = 0
                grabmultiplier2 = 1
            p1health = p1health - lifedrain2 * prevent
            if lifedrain2 > 0:
                prevent = 1
            p2health = p2health + lifedrain2
            seedcount2 = seedcount2 + seedincrement2
    if attacktype == "grab":
        if attacktype2 == "pass":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2
            if armorattack > 0:
                p2health = p2health - (armor + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2
                armor = 0
            if damage > 0 or armorattack > 0:
                tauntboost = 1
                blockboost = 0
                prevent2 = 1
                grabmultiplier = 1
            seedcount = seedcount + seedincrement
            p2health = p2health - lifedrain * prevent2
            if lifedrain > 0:
                prevent2 = 1
            p1health = p1health + lifedrain
        if attacktype2 == "taunt":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * grabmultiplier * seedboost * tauntkiller * prevent2
            if armorattack > 0:
                p2health = p2health - (armor + blockboost) * tauntboost * grabmultiplier * seedboost * tauntkiller * prevent2
                armor = 0
            if damage > 0 or armorattack > 0:
                tauntboost = 1
                blockboost = 0
                prevent2 = 1
                grabmultiplier = 1
            seedcount = seedcount + seedincrement
            p2health = p2health - lifedrain * prevent2
            if lifedrain > 0:
                prevent2 = 1
            p1health = p1health + lifedrain
        if attacktype2 == "strong":
            if removera12 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                prevent = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - (lifeheal2 + blockboost2 + lifedrain2) * healmultiplier2 * tauntboost2 * seedboost2 * prevent
                    healmultiplier2 = 1
                    prevent = 1
                    healcon2 = 0
            else:
                p2health = p2health + (lifeheal2 + lifedrain2) * healmultiplier2
                p1health = p1health - lifedrain2 * healmultiplier2
                if lifeheal2 > 0:
                    healmultiplier2 = 1
            tauntboost2 = 1
            trueblockability2 = 0
            seedcount2 = seedcount2 + seedincrement2
            blockboost2 = 0
            grabmultiplier = 1
            tauntboost = 1
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
        if attacktype2 == "light":
            if removera22 == 1:
                wasted = 1
                return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2
            if damage2 > 0:
                p1health = p1health - (damage2 + blockboost2) * tauntboost2 * seedboost2 * prevent
                prevent = 1
                tauntboost2 = 1
                trueblockability2 = 0
                blockboost2 = 0
                grabmultiplier = 1
            if armorgain2 > 0:
                armor2 = armor2 + armorgain2 * armormultiplier2
                armormultiplier2 = 1
            if healcon2 == 1:
                if lifeheal2 > 0:
                    p1health = p1health - ((lifeheal2 + blockboost2) * healmultiplier2 * tauntboost2 * seedboost2) * prevent
                    healmultiplier2 = 1
                    healcon2 = 0
                    blockboost2 = 0
                    prevent = 1
            else:
                p2health = p2health + lifeheal2 * healmultiplier2
                if lifeheal2 != 0:
                    healmultiplier2 = 1
            tauntboost = 1
        if attacktype2 == "shield":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2 * grabweakness2
            if armorattack > 0:
                p2health = p2health - (armor + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2 * grabweakness2
                armor = 0
            if damage > 0 or armorattack > 0:
                tauntboost = 1
                prevent2 = 1
                blockboost = 0
                grabmultiplier = 1
            p2health = p2health - lifedrain * prevent2
            if lifedrain > 0:
                prevent2 = 1
            p1health = p1health + lifedrain
            seedcount = seedcount + seedincrement
        if attacktype2 == "counter":
            if damage > 0:
                p2health = p2health - (damage + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2
            if armorattack > 0:
                p2health = p2health - (armor + blockboost) * tauntboost * grabmultiplier * seedboost * prevent2
                armor = 0
            if damage > 0 or armorattack > 0:
                tauntboost = 1
                prevent2 = 1
                blockboost = 0
                grabmultiplier = 1
            p2health = p2health - lifedrain * prevent2
            seedcount = seedcount + seedincrement
            if lifedrain > 0:
                prevent2 = 1
            p1health = p1health + lifedrain
        if attacktype2 == "grab":
            if attackspeed < attackspeed2:
                if damage > 0:
                    p2health = p2health - (damage + blockboost) * tauntboost * grabmultiplier * seedboost * grabweakness2 * prevent2
                if armorattack > 0:
                    p2health = p2health - (armor + blockboost) * tauntboost * grabmultiplier * seedboost * grabweakness2 * prevent2
                    armor = 0
                if damage > 0 or armorattack > 0:
                    tauntboost = 1
                    prevent2 = 1
                    blockboost = 0
                    grabmultiplier = 1
                p2health = p2health - lifedrain * prevent2
                if lifedrain > 0:
                    prevent2 = 1
                p1health = p1health + lifedrain
                seedcount = seedcount + seedincrement
            if attackspeed > attackspeed2:
                if damage2 > 0:
                    p1health = p1health - (damage2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * grabweakness * prevent
                if armorattack2 > 0:
                    p1health = p1health - (armor2 + blockboost2) * tauntboost2 * grabmultiplier2 * seedboost2 * grabweakness * prevent
                    armor2 = 0
                if damage2 > 0 or armorattack2 > 0:
                    tauntboost2 = 1
                    prevent = 1
                    blockboost2 = 0
                    grabmultiplier2 = 1
                p1health = p1health - lifedrain2 * prevent
                if lifedrain2 > 0:
                    prevent = 1
                p2health = p2health + lifedrain2
                seedcount2 = seedcount2 + seedincrement2
            grabmultiplier2 = 1
            grabmultiplier = 1
            tauntboost2 = 1
            tauntboost = 1
    if seedcount > (seedmax-1):
        value = min((seedcount-a), (seedcount-seedmax))
        p1health = p1health + value
    if seedcount2 > (seedmax-1):
        value = min((seedcount2-b), (seedcount2-seedmax))
        p2health = p2health + value
        # trackervalue start, comment this or at beginning of battle
    if gametracker == 0 and seedcount2 > (seedmax-1):
        tracker = tracker + 1
        gametracker = 1
        # trackervalue end
    return p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2


def turnOccurence(k1,k2,p1win,p2win,counter,tracker,p1health,p2health,tauntboost,tauntboost2,seedcount,seedcount2,blockboost,blockboost2,trueblockability,trueblockability2,removera1,removera2,removera12,removera22,gametracker,wasted,tauntvalue,tauntvalue2,healmultiplier,healmultiplier2,grabmultiplier,grabmultiplier2,healcon,healcon2,armormultiplier,armormultiplier2,armor,armor2,prevent,prevent2,pick1,pick2):
    if p1health > k1:
        p1health = k1
    if p2health > k2:
        p2health = k2
    static1 = removera1
    static2 = removera2
    static3 = removera12
    static4 = removera22
    # print(pick1, pick2)
    prep1 = p1health
    prep2 = p2health
    attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healattribute, grabweakness, grabattribute, healconattribute, healcounter, hitlessheal, tauntvtauntdamage, armormultiplierattribute, armorgain, armorattack, counterbonus, tauntnegation, preventattribute = attributize(
        pick1)
    attacktype2, attackspeed2, damage2, attackmultiplier2, lifeheal2, countervalue2, lifedrain2, counterweakness2, seedincrement2, blockpenalty2, blockbooster2, blockability2, tauntkiller2, shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healattribute2, grabweakness2, grabattribute2, healconattribute2, healcounter2, hitlessheal2, tauntvtauntdamage2, armormultiplierattribute2, armorgain2, armorattack2, counterbonus2, tauntnegation2, preventattribute2 = attributize(
        pick2)
    p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2 = battle(
        attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, seedcount, lifedrain,
        counterweakness, seedincrement, blockpenalty, blockbooster, blockboost, blockability, trueblockability,
        tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healmultiplier,
        healattribute, grabweakness, grabattribute, healconattribute, healcounter, attacktype2, attackspeed2,
        damage2, attackmultiplier2, lifeheal2, countervalue2, seedcount2, lifedrain2, counterweakness2,
        seedincrement2, blockpenalty2, blockbooster2, blockboost2, blockability2, trueblockability2, tauntkiller2,
        shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healmultiplier2, healattribute2,
        grabweakness2, grabattribute2, healconattribute2, healcounter2, p1health, p2health, tauntboost, tauntboost2,
        tracker, gametracker, removera1, removera2, removera12, removera22, tauntvalue, tauntvalue2, grabmultiplier,
        grabmultiplier2, healcon, healcon2, hitlessheal, hitlessheal2, tauntvtauntdamage, tauntvtauntdamage2,
        armormultiplier, armormultiplier2, armorgain, armorgain2, armor, armor2, armorattack, armorattack2,
        armormultiplierattribute, armormultiplierattribute2, counterbonus, counterbonus2, tauntnegation,
        tauntnegation2, preventattribute, preventattribute2, prevent, prevent2)
    removera1, removera2, removera12, removera22 = wastecheck(wasted, removera1, removera2, removera12, removera22,
                                                              remover, remover2, static1, static2, static3, static4)
    p1health, p2health, armor, armor2 = healthtoarmorswitch(prep1, prep2, p1health, p2health, armor, armor2)
    #print("p1health", p1health, "p2health", p2health, "armor",armor, "armor2", armor2)
    p1win, p2win = gameendwind(p1health, p2health)
    return(k1,k2,p1win,p2win,counter,tracker,p1health,p2health,tauntboost,tauntboost2,seedcount,seedcount2,blockboost,blockboost2,trueblockability,trueblockability2,removera1,removera2,removera12,removera22,gametracker,wasted,tauntvalue,tauntvalue2,healmultiplier,healmultiplier2,grabmultiplier,grabmultiplier2,healcon,healcon2,armormultiplier,armormultiplier2,armor,armor2,prevent,prevent2)



def simgame():
    k1 = 25
    k2 = 25
    p1win = 0
    p2win = 0
    counter = 0
    tracker = 0
    p1health = k1
    p2health = k2
    tauntboost = 1
    tauntboost2 = 1
    seedcount = 0
    seedcount2 = 0
    blockboost = 0
    blockboost2 = 0
    trueblockability = 0
    trueblockability2 = 0
    removera1 = 0
    removera2 = 0
    removera12 = 0
    removera22 = 0
    gametracker = 0
    wasted = 0
    tauntvalue = 0
    tauntvalue2 = 0
    healmultiplier = 1
    healmultiplier2 = 1
    grabmultiplier = 1
    grabmultiplier2 = 1
    healcon = 0
    healcon2 = 0
    armormultiplier = 1
    armormultiplier2 = 1
    armor = 0
    armor2 = 0
    prevent = 1
    prevent2 = 1
    while p1health > 0 and p2health > 0:
        if p1health > k1:
            p1health = k1
        if p2health > k2:
            p2health = k2
        static1 = removera1
        static2 = removera2
        static3 = removera12
        static4 = removera22
        pick1 = realplayerpick()
        pick2 = realplayerpick()
        #print(pick1, pick2)
        prep1 = p1health
        prep2 = p2health
        attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healattribute, grabweakness, grabattribute, healconattribute, healcounter, hitlessheal, tauntvtauntdamage, armormultiplierattribute, armorgain, armorattack, counterbonus, tauntnegation, preventattribute = attributize(
            pick1)
        attacktype2, attackspeed2, damage2, attackmultiplier2, lifeheal2, countervalue2, lifedrain2, counterweakness2, seedincrement2, blockpenalty2, blockbooster2, blockability2, tauntkiller2, shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healattribute2, grabweakness2, grabattribute2, healconattribute2, healcounter2, hitlessheal2, tauntvtauntdamage2, armormultiplierattribute2, armorgain2, armorattack2, counterbonus2, tauntnegation2, preventattribute2 = attributize(
            pick2)
        p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2 = battle(
            attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, seedcount, lifedrain,
            counterweakness, seedincrement, blockpenalty, blockbooster, blockboost, blockability, trueblockability,
            tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healmultiplier,
            healattribute, grabweakness, grabattribute, healconattribute, healcounter, attacktype2, attackspeed2,
            damage2, attackmultiplier2, lifeheal2, countervalue2, seedcount2, lifedrain2, counterweakness2,
            seedincrement2, blockpenalty2, blockbooster2, blockboost2, blockability2, trueblockability2, tauntkiller2,
            shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healmultiplier2, healattribute2,
            grabweakness2, grabattribute2, healconattribute2, healcounter2, p1health, p2health, tauntboost, tauntboost2,
            tracker, gametracker, removera1, removera2, removera12, removera22, tauntvalue, tauntvalue2, grabmultiplier,
            grabmultiplier2, healcon, healcon2, hitlessheal, hitlessheal2, tauntvtauntdamage, tauntvtauntdamage2,
            armormultiplier, armormultiplier2, armorgain, armorgain2, armor, armor2, armorattack, armorattack2,
            armormultiplierattribute, armormultiplierattribute2, counterbonus, counterbonus2, tauntnegation,
            tauntnegation2, preventattribute, preventattribute2, prevent, prevent2)
        removera1, removera2, removera12, removera22 = wastecheck(wasted, removera1, removera2, removera12, removera22,
                                                                  remover, remover2, static1, static2, static3, static4)
        p1health, p2health, armor, armor2 = healthtoarmorswitch(prep1, prep2, p1health, p2health, armor, armor2)
        print("p1health", p1health, "p2health", p2health)
        p1win, p2win = gameend(p1health, p2health, p1win, p2win)
    print("player 1 won " + str(p1win) + " games")



if __name__ == "__main__":
    Simulation = False # This lets players play when false
    windowskip = True#skips to window game when true
    while windowskip == True:
        BotPlay = False#Play against bot
        window(BotPlay)
    if Simulation == False: # this simulates
        simgame()
    howmany = int(input("How many games do you want to test?"))
    strategy = input("give strategy using the table of values, separated by a comma no spaces") # makes player1 start each game with this
    stratlist = strategy.split(",")
    t0= time.perf_counter()
    print(stratlist)
    k = len(stratlist)
    preset = 1#This is first players character for simulations.
    preset2 = 1#This is second players character for simulations.
    #Note:v1a1 does not gain life on t
    for j in range(0,1):
        preset2 = j+1
        p1win = 0
        p2win = 0
        k1 = 27 #player1 health(useful to put at 2 higher than intial to test openers)
        k2 = 27 #player2 health
        counter = 0
        tracker = 0#use to track how often an occurence occurs
        for i in range(0, howmany):
            #Beginning of each game
            p1health = k1-2
            p2health = k2-2
            counter = 0
            tauntboost = 1
            tauntboost2 = 1
            seedcount = 0
            seedcount2 = 0
            blockboost = 0
            blockboost2 = 0
            trueblockability = 0
            trueblockability2 = 0
            removera1 = 0
            removera2 = 0
            removera12 = 0
            removera22 = 0
            gametracker = 0
            wasted = 0
            tauntvalue = 0
            tauntvalue2 = 0
            healmultiplier = 1
            healmultiplier2 = 1
            grabmultiplier = 1
            grabmultiplier2 = 1
            healcon = 0
            healcon2 = 0
            armormultiplier = 1
            armormultiplier2 = 1
            armor = 0
            armor2 = 0
            prevent = 1
            prevent2 = 1
            while p1health > 0 and p2health > 0:
                if p1health > k1:
                    p1health = k1
                if p2health > k2:
                    p2health = k2
                static1 = removera1
                static2 = removera2
                static3 = removera12
                static4 = removera22
                pick1 = playerpick(counter, stratlist, 0, tauntboost, tauntboost2, trueblockability, trueblockability2,preset)
                pick2 = playerpick(counter, stratlist, -1, tauntboost, tauntboost2, trueblockability, trueblockability2,preset2)
                #print(pick1, pick2) #use for playtesting and debugging
                prep1 = p1health
                prep2 = p2health
                attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healattribute, grabweakness, grabattribute, healconattribute, healcounter, hitlessheal, tauntvtauntdamage, armormultiplierattribute, armorgain, armorattack, counterbonus, tauntnegation, preventattribute = attributize(pick1) #gets the attributes of a move
                attacktype2, attackspeed2, damage2, attackmultiplier2, lifeheal2, countervalue2, lifedrain2, counterweakness2, seedincrement2, blockpenalty2, blockbooster2, blockability2, tauntkiller2, shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healattribute2, grabweakness2, grabattribute2, healconattribute2, healcounter2, hitlessheal2, tauntvtauntdamage2, armormultiplierattribute2, armorgain2, armorattack2, counterbonus2, tauntnegation2, preventattribute2 = attributize(pick2) #gets attributes for player 2's moves
                p1health, p2health, tauntboost, tauntboost2, seedcount, seedcount2, blockboost, blockboost2, trueblockability, trueblockability2, removera1, removera2, removera12, removera22, tracker, gametracker, wasted, tauntvalue, tauntvalue2, healmultiplier, healmultiplier2, grabmultiplier, grabmultiplier2, healcon, healcon2, armormultiplier, armormultiplier2, armor, armor2, prevent, prevent2 = battle(attacktype, attackspeed, damage, attackmultiplier, lifeheal, countervalue, seedcount, lifedrain, counterweakness, seedincrement, blockpenalty, blockbooster, blockboost, blockability, trueblockability, tauntkiller, shieldnegate, remover, strongmultiplier, tauntincrement, tradeheal, healmultiplier, healattribute, grabweakness, grabattribute, healconattribute, healcounter, attacktype2, attackspeed2, damage2, attackmultiplier2, lifeheal2, countervalue2, seedcount2, lifedrain2, counterweakness2, seedincrement2, blockpenalty2, blockbooster2, blockboost2, blockability2, trueblockability2, tauntkiller2, shieldnegate2, remover2, strongmultiplier2, tauntincrement2, tradeheal2, healmultiplier2, healattribute2, grabweakness2, grabattribute2, healconattribute2, healcounter2, p1health, p2health, tauntboost, tauntboost2, tracker, gametracker, removera1, removera2, removera12, removera22, tauntvalue, tauntvalue2, grabmultiplier, grabmultiplier2, healcon, healcon2, hitlessheal, hitlessheal2, tauntvtauntdamage, tauntvtauntdamage2, armormultiplier, armormultiplier2, armorgain, armorgain2, armor, armor2, armorattack, armorattack2, armormultiplierattribute, armormultiplierattribute2, counterbonus, counterbonus2, tauntnegation, tauntnegation2, preventattribute, preventattribute2, prevent, prevent2) # this is the logic for the battle, most likely place for logic errors to occur.
                removera1, removera2, removera12, removera22 = wastecheck(wasted, removera1, removera2, removera12, removera22, remover, remover2, static1, static2, static3, static4) # this is used when a move can't be used due to v3b1, there's probably a better way to program this in.
                p1health, p2health, armor, armor2 = healthtoarmorswitch(prep1,prep2, p1health, p2health, armor, armor2) # I did this to rearrange armor, there are a couple of weird interactions here, like if player1 heals and gets hit for 2 but has 2 armor, they dobn't lose armor.
                #print("p1health", p1health, "p2health", p2health, "tauntboost", tauntboost, "seedcount2", seedcount2) # replace what's in here with what you want to keep track of, mainly for debugging and playtesting
                p1win, p2win = gameend(p1health, p2health, p1win, p2win) #this checks to see who wins, if both lose a tie is recorded
                counter = counter+1 #keeps track of game number
        tf = time.perf_counter()
        print(tf-t0)
        print("player 1 won " + str(p1win) + " games")
        print("player 2 won " + str(p2win) + " games")
        print("there were " + str(howmany-(p1win + p2win)) + " ties")
        print("The tracker ticked", str(tracker), "times. That is", str((float(tracker)/float(howmany)*100)), "percent of games.")