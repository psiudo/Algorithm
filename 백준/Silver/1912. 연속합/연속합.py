
"""
10만 * 10만 = 100억
완전탐색 불가, 순서가 정해져있는 수열이기에 정렬도 X
dp[x]를 다음과 같이 정의하자.
x로 끝나는 부분수열의 구간합의 최댓값
dp[x]에 대해서
이전까지 dp[x-1]가 최대라고 가정하자.
그럼 다음 수열에 대해서
dp[x] 입장에서 dp[x-1]을 유지할건지 새로 시작할건지 물으면 된다.
"""

n = int(input())
lst = list(map(int, input().split()))
dp = [0] * (n+1) # dp 테이블 / 0인덱스는 버림
dp[1] = lst[0]
for x, num in enumerate(lst, start = 1) :
    dp[x] = max( dp[x-1] + num, num )

print(max(dp[1:n+1]))