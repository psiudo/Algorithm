"""
맨 오른쪽에 1을 추가하는 것의 
수적 규칙성을 찾기 어려울 것
"""
A, B = map(int, input().split())
#####################################
def two_multiply(x) :
    return 2*x
def add_one(x) :
    return int(str(x) + '1')
#####################################
v = set()
def search(raw, target) :
    q = [(raw, 1)]
    while q :
        x, cnt = q.pop(0)
        if x == target :
            return cnt
        # 넘었다면
        if x > target :
            continue
        a, b = two_multiply(x), add_one(x)
        # 다음 후보들 역시 방문하지 않았다면
        if a not in v :
            q.append((a, cnt+1))
            v.add(a)
        if b not in v :
            q.append((b, cnt+1))
            v.add(b)

    return -1

#######################################
print(search(A, B))