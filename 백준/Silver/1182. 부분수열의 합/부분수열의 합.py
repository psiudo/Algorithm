N, S = map(int, input().split())
tot_set = list(map(int, input().split()))

result = []

# 부분수열을 찾는 함수
def find_subset(depth, ele_sum):
    if depth == N: # N개의 원소에 대해 모두 선택과 비선택 모두 했다면 = depth가 N까지 왔다면
        if ele_sum == S: #
            result.append(1)
        return

    find_subset(depth + 1, ele_sum + tot_set[depth]) # 해당 수열을 선택하거나
    find_subset(depth + 1, ele_sum) #선택하지 않을 수 있다.


find_subset(0, 0)
if S == 0:
    print(sum(result) - 1)
else:
    print(sum(result))