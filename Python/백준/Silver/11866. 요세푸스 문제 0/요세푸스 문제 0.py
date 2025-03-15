def josephus(N, K):
    arr = list(range(1, N + 1))
    result = []
    index = 0

    while arr:
        index = (index + K - 1) % len(arr)
        result.append(arr.pop(index))
    
    print("<" + ", ".join(map(str, result)) + ">")

N, K = map(int, input().split())
josephus(N, K)
