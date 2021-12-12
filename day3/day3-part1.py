path = 'day3/input.txt'

zeroes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ones = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open(path) as f:
     for line in f:
         i = 0
         for ch in line:
             if ch == '1':
                 zeroes[i] += 1
             else:
                 if ch == '0':
                    ones[i] += 1
             i+=1

gamma_rate   = ""
epsilon_rate = ""

for one, zero in zip(ones, zeroes):
    if one > zero:
        gamma_rate += "1"
        epsilon_rate += "0"
    else:
        gamma_rate += "0"
        epsilon_rate += "1"

grate = int(gamma_rate, 2)
erate = int(epsilon_rate, 2)

print(f"{grate} ({gamma_rate}) * {erate} ({epsilon_rate}) = {grate * erate}")