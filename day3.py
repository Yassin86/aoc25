data = open('test.txt').read().split('\n')

def joltage(x, p1):
    digits = [int(a) for a in x]
    ans = ''
    if p1:
        l = max(digits[:-1])
        ans += str(l)
        ans += str(max(digits[digits.index(l)+1:]))
        return int(ans)
    
    l = max(digits[:-12])
    ans += str(l)
    for i in range(1,12):
        l2 = max(digits[digits.index(l)+1:][:-(12-i)])
        ans += str(l2)
        l = l2
    print(int(ans))
    return int(ans)


p1 = 0
p2 = 0
for d in data:
    p1 += joltage(d, True)
    p2 += joltage(d, False)

print(p1)
print(p2)