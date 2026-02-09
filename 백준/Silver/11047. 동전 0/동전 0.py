N, K = map(int, input().split())
lst = []
for _ in range(N) :
    lst.extend( [int(input())] )
lst.sort(reverse=True) # 정렬까지 완료 in-place 함수

idx, cnt = 0, 0
while idx <= N-1 :
    if lst[idx] <= K :
        K -= lst[idx]
        cnt += 1
    else :
        idx += 1

    if K == 0 :
        break

print(cnt)