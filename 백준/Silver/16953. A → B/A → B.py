"""
맨 오른쪽에 1을 추가하는 것의 
수적 규칙성을 찾기 어려울 것
"""
A, B = map(int, input().split())
#####################################
def search(raw, target) :
    q = [(raw, 1)]
    while q :
        x, cnt = q.pop(0)
        if x == target :
            return cnt
        # 넘었다면
        if x > target :
            continue
        a, b = 2*x, 10*x + 1
        # 타겟보다 작으면 넣기
        if a <= target :
            q.append((a, cnt+1))
        if b <= target :
            q.append((b, cnt+1))

    return -1

#######################################
print(search(A, B))