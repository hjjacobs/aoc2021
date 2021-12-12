path = 'day1/input.txt'

with open(path) as f:
    depths = f.read().splitlines()

count = 0
previous = -1

# Skip first one
for depth in depths[1:]:
    if int(depth) > previous:
        count+=1

    previous = int(depth)

print(f">>> counted: {count}")