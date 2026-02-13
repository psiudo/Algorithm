from collections import deque

T = int(input())

wheels = []
for i in range(1, T+1) :
    wheels.append(deque(list(map(int, list(input())))))


def probe(who, drt) :
    drt_lst = [0]*T # T개의 톱니에 대한 방향 리스트
    drt_lst[who] = drt # 초기 톱니바귀
    l, r = who-1, who+1
    # l과 r은 현재 판단 중인 톱니바퀴
    while 0 <= l :
        if wheels[l][2] == wheels[l+1][6] :
            drt_lst[l] = 0
        elif wheels[l][2] != wheels[l+1][6] :
            drt_lst[l] = - drt_lst[l+1]
        l -= 1

    while r <= T-1 :
        if wheels[r-1][2] == wheels[r][6] :
            drt_lst[r] = 0
        elif wheels[r-1][2] != wheels[r][6] :
            drt_lst[r] = - drt_lst[r-1]
        r += 1
    return drt_lst


# 1은 시계방향, -1은 반시계 방향
def rotate_wheel(drt_lst) :
    for i in range(T) :
        if drt_lst[i] == 1 :
            wheels[i].rotate(1)
        elif drt_lst[i] == -1 :
            wheels[i].rotate(-1)

K = int(input())
for _ in range(K) :
    who, drt = map(int, input().split()) # 3 -1
    who = who - 1 # 0인덱스로
    rotate_drt = probe(who, drt)
    rotate_wheel(rotate_drt)

# ===============================================
ans = 0
for wheel in wheels :
    if wheel[0] == 1 :
        ans += 1
print(ans)