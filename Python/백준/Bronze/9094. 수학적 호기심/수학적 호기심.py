def count_valid_pairs(n, m):
    count = 0
    for a in range(1, n):
        for b in range(a + 1, n):
            if (a**2 + b**2 + m) % (a * b) == 0:
                count += 1
    return count

# 입력 처리
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    result = count_valid_pairs(n, m)
    print(result)
