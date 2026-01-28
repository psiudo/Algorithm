######################################
N, M = map(int, input().split())

grid = [[]*M for _ in range(N)]
for row in range(N) :
    st = input()
    for s in st :
        if s == "B" :
            grid[row].append(1)
        else :
            grid[row].append(0)

######################################
########################## 검은색이 1 ############################
check1 = [] # 흰색시작
for i in range(M) :
    if i % 2 == 1 :
        check1.append(1)
    else :
        check1.append(0)
check2 = [] #검은색시작
for i in range(M) :
    if i % 2 == 1 :
        check2.append(0)
    else :
        check2.append(1)
#######################################
ans = []
for x in range(N+1-8) :
    for y in range(M+1-8) :
        cnt1 = 0
        cnt2 = 0
        for i in range(8) :
            for j in range(8) :
                if i%2 == 0 :
                    if grid[x+i][y+j] != check2[j] :
                        cnt1 += 1
                    else :
                        cnt2 += 1
                else :
                    if grid[x+i][y+j] != check1[j] :
                        cnt1 += 1
                    else :
                        cnt2 += 1
        cnt3 = 0
        cnt4 = 0
        for i in range(8) :
            for j in range(8) :
                if i%2 == 0 :
                    if grid[x+i][y+j] != check1[j] :
                        cnt3 += 1
                    else :
                        cnt4 += 1
                else :
                    if grid[x+i][y+j] != check2[j] :
                        cnt3 += 1
                    else :
                        cnt4 += 1
        ans.append(min(cnt1, cnt2, cnt3, cnt4))

print(min(ans))