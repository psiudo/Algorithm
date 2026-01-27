T = int(input())
for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, list(map(str, input())))) for _ in range(N)]

    ans = 0
    for i in range(N//2) :
        k = i*2 + 1
        start = (N - k)//2

        for col in range(start, start+k):
            ans += arr[i][col]
            ans += arr[N-1-i][col]


    ans += sum(arr[N//2])
    print(f'#{tc} {ans}')