L, N, T = map(int, input().split())

pos = []
dirv = []
for _ in range(N):
    s, c = input().split()
    s = int(s)
    pos.append(s)
    dirv.append(1 if c == 'R' else -1)

ans = 0

for _ in range(T):
    # 1) 1초 이동 + 벽 반사만 처리
    for i in range(N):
        pos[i] += dirv[i]
        if pos[i] == 0 or pos[i] == L:
            dirv[i] *= -1

    # 2) 같은 위치에 모인 개수로 충돌 수 카운트
    cnt = {}
    for p in pos:
        cnt[p] = cnt.get(p, 0) + 1

    for k in cnt.values():
        ans += k * (k - 1) // 2

print(ans)