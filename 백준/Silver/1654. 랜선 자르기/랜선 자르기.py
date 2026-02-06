"""
읽기 + 구상 : 3:00 / 코드 : 15:00 /디버깅 : / 실패횟수 : / 제출횟수 : 1/
"""

"""
그러니까 N개를 만들어야 하는데,,, 그 N개의 랜선의 길이 길었으면 좋겠다.
이분 탐색으로 31번 정도의 연산을 10000개에 대해서 
"""
K, N = map(int, input().split())
lst = []
for _ in range(K) :
    lst.append(int(input()))

L, R = 0, max(lst)+1 # 해가 [L, R)에 있다.
while L < R :
    curr_sum = 0
    cut_len = (L + R)//2
    for each in lst :
        curr_sum += (each//cut_len) # 어떤 길이에 대해서 나올 수 있는 한 랜선의 갯수

    if N <= curr_sum :
        L = cut_len + 1
    elif curr_sum < N :
        R = cut_len

print(L-1)