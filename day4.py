data = open('day4.txt').read().split('\n')
data = [list(d) for d in data]

p1 = 0
output = 0
coords = []
passes = {}
counter = 0
while True:
    counter += 1
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] != '@':
                continue
            count = 0
            for a in range(-1,2):
                for b in range(-1, 2):
                    if a == 0 and b == 0:
                        continue
                    ni, nj = i + a, j + b
                    if 0 <= ni < len(data) and 0 <= nj < len(data[ni]):
                        if data[ni][nj] == '@':
                            count += 1
            if count < 4:
                coords.append((i,j))
                output += 1
    for i,j in coords:
        data[i][j] = '.'
    passes[counter] = output
    if counter == 1:
        p1 = output
    if output == 0:
        break
    output = 0

print(p1)
print(sum(passes.values()))