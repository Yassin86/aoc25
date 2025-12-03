data = open('day2.txt').read().split(',')

def find_invalid_p1(i, j):
    out = []
    for x in range(i, j+1):
        strx = str(x)
        chars = len(strx)
        if chars % 2 != 0:
            continue
        if strx[:chars//2] == strx[chars//2:]:
            out.append(x)
    return sum(out)

def find_invalid_p2(i, j):
    out = []
    for x in range(i, j+1):
        strx = str(x)
        chars = len(strx)
        for z in range(1,chars//2+1):
            if x in out:
                break
            if strx[:z] * (chars//z) == strx:
                out.append(x)
    return sum(out)

p1=[]
p2=[] 
for pair in data:
    ranges = pair.split('-')
    i, j = int(ranges[0]), int(ranges[1])
    p1.append(find_invalid_p1(i,j))
    p2.append(find_invalid_p2(i,j))

print(sum(p1))
print(sum(p2))
