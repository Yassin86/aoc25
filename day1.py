data = open('day1.txt').read().split('\n')
# part 1 - nice
operation_map = {'L':'-', 'R':'+'}
num = 50
p1 = 0
for i in data:
    dir, amount = i[0], i[1:]
    num = eval(str(num) + operation_map.get(dir) + amount) % 100
    if num == 0:
        p1 += 1

print('part 1: %s' % p1)

# part 1 and 2 - horrible
num = 50
p11 = 0
p2 = 0
for i in data:
    dir, amount = i[0], i[1:]
    for x in range(int(amount)):
        num = eval(str(num)+operation_map.get(dir)+'1') % 100
        if num == 0:
            p2 += 1
    if num == 0:
        p11 += 1

print('part 1 method 2: %s' % p11)
print('part 2: %s' % p2)