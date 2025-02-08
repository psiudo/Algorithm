lines = []
max_len = 0
for _ in range(5):
    line = input()
    lines.append(line)
    if len(line) > max_len :
        max_len = len(line)

vertical = ''
for col in range(max_len) :
    for line in lines :
        if len(line) > col :
            vertical += line[col]

print(vertical)