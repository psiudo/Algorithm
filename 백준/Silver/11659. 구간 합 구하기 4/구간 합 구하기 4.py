import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
x_list = []
y_list = []

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    x_list.append(x)
    y_list.append(y)

y_max = max(y_list)

DAT = [0] * (y_max + 1)
DAT[0] = num_list[0]

for i in range(1, y_max + 1):
    DAT[i] = DAT[i - 1] + num_list[i-1]

for j in range(M):
    print(DAT[y_list[j]] - DAT[x_list[j]-1])
