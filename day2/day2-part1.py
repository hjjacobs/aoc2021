path = 'day2/input.txt'

commands = []

with open(path) as f:
    for line in f:
       commands.append(line.split())

horizontal = 0
depth = 0

for command in commands:
    if command[0] == 'forward':
        horizontal += int(command[1])
    else:
        if command[0] == 'down':
            depth += int(command[1])
        else:
            if command[0] == 'up':
                depth -= int(command[1])

print(f">>> answer: {horizontal} x {depth} = {horizontal * depth}")