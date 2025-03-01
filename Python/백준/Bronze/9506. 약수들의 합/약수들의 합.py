while True:
    n = int(input())
    if n == -1:
        break

    divisors = []
    tot = 0
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
            tot += i

    if tot == n:
        print(f"{n} = {' + '.join(map(str, divisors))}")
    else:
        print(f"{n} is NOT perfect.")
