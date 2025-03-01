import math
M = int(input())
N = int(input())
if M < 2:
    M = 2
size = N - M + 1
is_prime = [True] * size
for i in range(2, int(math.sqrt(N)) + 1):
    start = max(i * i, ((M + i - 1) // i) * i)
    for j in range(start, N + 1, i):
        is_prime[j - M] = False
prime_numbers = []
for k in range(size):
    if is_prime[k]:
        prime_numbers.append(M + k)
if prime_numbers:
    print(sum(prime_numbers))
    print(prime_numbers[0])
else:
    print(-1)
