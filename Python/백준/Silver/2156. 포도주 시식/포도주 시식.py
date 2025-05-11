n = int(input())
wine_arr = [0] * (n + 1)
for i in range(1, n + 1):
    wine_arr[i] = int(input())

dp = [0] * (n + 1)
dp[1] = wine_arr[1]
if n >= 2:
    dp[2] = wine_arr[1] + wine_arr[2]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 1],
        dp[i - 2] + wine_arr[i],
        dp[i - 3] + wine_arr[i - 1] + wine_arr[i]
    )

print(dp[n])
