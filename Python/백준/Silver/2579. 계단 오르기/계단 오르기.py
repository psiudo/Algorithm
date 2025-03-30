N = int(input())
stairs = []
for _ in range(N) :
    stairs.append(int(input()))

dp = [[0]*2 for _ in range(N)]

dp[0][0] = stairs[0]
if N >= 2:
    dp[1][0] = stairs[1]
    dp[1][1] = stairs[0] + stairs[1]

for i in range(2, N) :
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[N-1]))