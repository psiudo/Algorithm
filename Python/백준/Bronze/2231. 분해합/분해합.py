def decomp(t, sum):
    if t == 0:
        return sum
    return decomp(t // 10, sum + t % 10)

n = int(input())

for i in range(max(1, n - 9 * len(str(n))), n):  
    if decomp(i, i) == n:
        print(i)
        break
else:
    print(0)
