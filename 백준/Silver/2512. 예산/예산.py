"""
읽기 + 구상 :  / 코드 : 10:00 / 디버깅 : 0 / 실패횟수 : / 제출횟수 : 2
"""

"""
상한액은 이진탐색으로 잡고 리스트 순회하면서 상한액보다 작은 것은 그대로 더하고
큰 것은 상한액으로 tot에 더해서 
만약 전체예산보다 
1) 작거나 같으면 상한액 올리고 
2) 크면 상한액을 내린다.
"""

N = int(input())
lst = list(map(int, input().split()))
max_budget = int(input())

# [l, r) 안에 목표 m이 있다.
# r을 max(lst)바로 오른쪽으로 정의한다.
l, r = 0, max(lst)+1
# 그러면 다음과 같이 l < r일 때까지 탐색하면 된다.
# 만약 while문을 벗어나면 바로 l = r이 되는 순간이고 바로 l-1 = r-1 = ans
while l < r :
    bound = (l + r)//2 # m은 상한액
    curr_sum = 0
    for each in lst :
        curr_sum += (bound if each >= bound else each)

    # curr_sum == max_budget인 경우를 생각해보자.
    # 1) r을 낮춘다면, 처음에 정의한 반열린구간 [l, r)의 정의에 위배된다.
    # 2) 아무것도 하지 않는다면 무한루프이다.
    # 3) 따라서 l을 올려서 무한루프도 해결하고 while문에 빠져나오면 된다.
    # 필연적인 이유는 현재 값을 정답 후보로 확정 짓고(Keep)
    # 더 큰 욕심을 부리기 위해 필연적으로 l이 올라가야 한다.
    # print를 l-1 또는 r-1로 찍었기 때문.
    if curr_sum <= max_budget :
        l = bound + 1
    elif curr_sum > max_budget :
        r = bound

print(r-1) # = l-1