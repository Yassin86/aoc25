data = open('test.txt').read().split('\n\n')
ranges, ing = data[0].split('\n'), data[1].split('\n')
ing = [int(a) for a in ing]

fresh = {}
for e, x in enumerate(ranges):
    start, end = x.split('-')
    v = fresh.get(int(start))
    if not v:
        fresh[int(start)] = int(end)
        continue
    if int(end) > v:
        fresh[int(start)] = int(end)
    else:
        fresh[int(start)] = v
        
# p1
ans = set()
for i in ing:
    for k,v in fresh.items():
        if i >= k and i<=v:
            ans.add(i)

# p2
ranges_list = sorted(fresh.items())
merged = []

for start, end in ranges_list:
    if merged and start <= merged[-1][1] + 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

p2 = sum(v - k + 1 for k, v in merged)

print(len(ans))
print(p2)