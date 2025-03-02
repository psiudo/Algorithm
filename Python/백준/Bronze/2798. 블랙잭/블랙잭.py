N, M = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()
best = 0

for i in range(N - 2):
    j, k = i + 1, N - 1
    while j < k:
        total = cards[i] + cards[j] + cards[k]
        if total > M:
            # 총합이 목표보다 크면, k를 줄여서 합을 감소시킴
            k -= 1
        else:
            # 총합이 목표 이하면, 현재 합이 최적이면 갱신하고, j를 증가시켜 더 큰 합을 시도
            best = max(best, total)
            if best == M:  # 최적해를 찾았으면 바로 종료
                print(best)
                exit()
            j += 1

print(best)
