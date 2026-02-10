"""
dp[x] = x까지 왔을 때의 최대 점수라 정의하자.
"""

N = int(input()) # 1 <= N <= 300
lst = []
for _ in range(N) :
    lst.append(int(input()))
# ========================================
dp = [0]*(len(lst))
if N >= 3 :
    dp[0] = lst[0]
    dp[1] = lst[0] + lst[1]
    dp[2] = max(lst[0] + lst[2], lst[1] + lst[2])
    for idx in range(3, N) :
        dp[idx] = max(dp[idx-3] + lst[idx-1], dp[idx-2]) + lst[idx]

    print(dp[N-1])
if N <= 2 :
    print(sum(lst))
