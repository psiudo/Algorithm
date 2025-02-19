H, W = map(int, input().split())
sky = []

for i in range(H) :
    line = input()
    temp = []
    for j in line :
        if j == 'c' :
            temp.append(0)
        else :
            temp.append(-1)
    sky.append(temp)

for p in range(H) :
    for q in range(1, W) :
        if sky[p][q] == 0 :
            continue
        if sky[p][q-1] != -1 :
            sky[p][q] = sky[p][q-1] + 1

for k in range(H) :
    print(*sky[k])