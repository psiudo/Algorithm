a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 < c:
    # n >= n0에서 조건이 최대값은 n=n0일 때 발생하므로 n0에서 f(n0) 조건을 체크
    if a1 * n0 + a0 <= c * n0:
        print(1)
    else:
        print(0)
elif a1 == c:
    print(1 if a0 <= 0 else 0)
else:
    print(0)
