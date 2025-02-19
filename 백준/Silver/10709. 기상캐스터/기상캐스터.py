
H, W = map(int, input().split())
sky = []
for _ in range(H) :
    sky.append(input()) # sky는 문자열

answer = [[-1]* W for _ in range(H)]

for i in range(H) :
    for j in range(W) :

        if sky[i][j] == 'c' :
            answer[i][j] = 0

            k = 1
            dist = 1
            while j + k <= W-1 :
                if sky[i][j+k] == '.' :
                    answer[i][j + k] = dist
                    dist += 1
                elif sky[i][j+k] == 'c' :
                    break
                k += 1

for q in range(H) :
    print(*answer[q])


