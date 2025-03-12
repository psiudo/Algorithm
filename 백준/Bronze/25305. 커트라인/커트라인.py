N, k = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(N - 1):
    max_idx = i
    for j in range(i + 1, N):
        if scores[j] > scores[max_idx]:  # 내림차순 정렬
            max_idx = j
    scores[i], scores[max_idx] = scores[max_idx], scores[i]

print(scores[k - 1])
