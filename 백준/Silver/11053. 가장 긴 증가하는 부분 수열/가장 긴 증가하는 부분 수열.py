N = int(input()) # 1 <= N <= 1000
lst = list(map(int, input().split())) # 10 20 10 30 20 50

"""
방만한 주석,,, 시작
dp문제인지는 알겠는데,,, 연속도 아니고 그렇기 때문에,,,
어떻게 정의할지 모르겠다... 고민중
dp는 현재 보고 있는 값이 이전의 값들로부터 확정돼야 한다.
그런데 이 문제에서는 새로 시작하는 것이 이득일 수도 있다.
dp[x]에 대해서 생각하자.
높이라는 state를 저장하는 것이 옳을 것 같다.
각 시작점에서 나올 수 있는 최대 증가 수열 길이를 구하면 된다.
하나의 축이 더해지니까 2차원 배열로 dp를 만들면 될 것 같다.
"""
dp = [ [0]*(N) for _ in range(N) ]

for row in range(N) :
    dp[row][row] = 1
    for col in range(row) :
        if lst[col] < lst[row] :
            dp[row][col] = max(dp[col]) + 1
        else :
            dp[row][col] = 0

print(max(max(row) for row in dp))