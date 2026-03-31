with open('RPSBattle.py', 'r') as f:
    content = f.read()

marker = '\nSimulation = False # This lets players play when false'
idx = content.find(marker)
if idx == -1:
    print('MARKER NOT FOUND')
else:
    before = content[:idx]
    after = content[idx + 1:]  # skip the leading \n
    indented = []
    for line in after.split('\n'):
        if line.strip():
            indented.append('    ' + line)
        else:
            indented.append('')
    new_content = before + '\n\nif __name__ == "__main__":\n' + '\n'.join(indented)
    with open('RPSBattle.py', 'w') as f:
        f.write(new_content)
    print('Done! Lines:', len(new_content.splitlines()))
