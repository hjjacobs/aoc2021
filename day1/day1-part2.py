import more_itertools

path = 'day1/input.txt'

depths = []

with open(path) as f:
    for line in f:
        depths.append(int(line))

windows = list(more_itertools.windowed(depths,3))

count = -1
previous = -1

for window in windows:
    Sum = sum(window)

    if Sum > previous:
        count+=1

    previous = Sum

print(f">>> counted: {count}")
