def facto (N) :
    if N == 0 :
        return 1
    return N*facto(N-1)

N = int(input())

print(facto(N))