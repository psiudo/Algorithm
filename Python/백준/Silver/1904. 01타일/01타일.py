import sys

sys.setrecursionlimit(10 ** 4)

MOD = 15746


def mat_mul(A, B):
    """2x2 정수 행렬 A, B를 곱한 결과 (mod 15746) 반환"""
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD,
            (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD,
            (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
        ]
    ]


def mat_pow(M, n):
    """2x2 행렬 M^n (mod 15746)을 분할 정복 (재귀)으로 계산"""
    if n == 1:
        return M

    # 절반 거듭제곱
    half = mat_pow(M, n // 2)
    half_sq = mat_mul(half, half)

    if n % 2 == 0:
        return half_sq
    else:
        return mat_mul(half_sq, M)


def fib(n):
    """
    표준 피보나치 Fib(n) (mod 15746).
    Fib(1) = 1, Fib(2) = 1, Fib(3) = 2 ...
    """
    if n == 1 or n == 2:
        return 1
    # F^(n-1) 계산
    F = [[1, 1], [1, 0]]
    Fn = mat_pow(F, n - 1)  # 깊이 O(log n)
    return Fn[0][0] % MOD  # fib(n)


def solve():
    input = sys.stdin.readline
    N = int(input())
    # 01타일 dp[N] = fib(N+1) (mod 15746)
    print(fib(N + 1) % MOD)

# 주석 제거하고 제출 시
solve()
