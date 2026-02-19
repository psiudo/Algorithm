MOD = 1000
N, B = map(int, input().split())
mat = [ list(map(lambda x: int(x) % MOD, input().split())) for _ in range(N) ]
def mat_mul(P, Q) :
    global MOD

    row = len(P)
    mid = len(P[0]) # = len(Q)
    col = len(Q[0])

    Q = list(map(list, zip(*Q)))
    res = [ [0] * col for _ in range(row) ]

    for i in range(row):
        for j in range(col):
            element = 0
            for t in range(mid):
                element = (element + P[i][t] * Q[j][t]) % MOD
            res[i][j] = element

    return res

def mat_pow(mat, B) :
    if B == 1 :
        return mat

    half = mat_pow(mat, B//2)
    half_mul = mat_mul(half, half)
    if not (B % 2):
        return half_mul

    else :
        return mat_mul(half_mul, mat)

ans = mat_pow(mat, B)
print('\n'.join(' '.join(map(str, row)) for row in  ans))