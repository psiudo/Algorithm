######################################
N, M = map(int, input().split())
grid = []
for _ in range(N):
    st = input()
    row = []
    for ch in st:
        row.append(int(ch == 'B'))
    grid.append(row)
######################################
########################## 검은색이 1 ############################
check1 = [1 if i % 2 else 0 for i in range(M)]
check2 = [0 if i % 2 else 1 for i in range(M)]

ans = 64
for x in range(N+1-8) :
    for y in range(M+1-8) :
        cntB = 0
        for i in range(8):
            row = grid[x+i][y:y+8]
            pattern = check2[y:y+8] if i % 2 == 0 else check1[y:y+8]
            cntB += sum(a ^ b for a, b in zip(row, pattern))

        ans = min(ans, cntB, 64 - cntB)

print(ans)