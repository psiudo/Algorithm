N, K = map(int, input().split())
coins = []
for _ in range(N) :
    coins.append(int(input()))

# K보다 작은 최초의 coin 찾기
for idx, coin in enumerate(coins[::-1]) :
    if K >= coin :
        break

# idx는 N - 1에서 가장 먼저 break 걸린 것을 빼면 된다.
idx = N - 1 - idx
cnt = 0
while K > 0 : # K == 0 이라면 종료되도록
    if coins[idx] > K :
        idx -= 1
        continue
    cnt += K // coins[idx]
    K = K % coins[idx]

print(cnt)