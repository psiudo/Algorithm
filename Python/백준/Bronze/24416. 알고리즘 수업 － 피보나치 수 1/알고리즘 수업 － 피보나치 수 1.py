def solve():
    n = int(input())

    f = [0] * (max(3, n + 1))
    f[0] = 0
    f[1] = 1
    f[2] = 1
    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    code1 = f[n]
    code2 = (n - 2)
    print(code1, code2)

solve()
