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

ans = set()
for i in ing:
    for k,v in fresh.items():
        if i >= k and i<=v:
            ans.add(i)

print(len(ans))