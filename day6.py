data = open('test.txt').read().split('\n')
data = [list(x) for x in data]

# Remove columns that are entirely empty
num_cols = len(data[0]) if data else 0
cols_to_keep = []
for col in range(num_cols):
    if any(row[col] != ' ' for row in data if col < len(row)):
        cols_to_keep.append(col)

data = [[row[col] for col in cols_to_keep] for row in data]
for d in data:
    print(d)