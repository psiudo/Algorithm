N1, N2 = map(int, input().split())
"""
1) 개미의 state는 위치와 방향
2) 1초 후에 dx의 합이 서로 0인 개미들의 위치를 교환한다.
3) 단, 1 -1 인 경우에만 (-1, 1)은 서로 갈 길 가는 경우 
4) 중복되는 알파벳은 없다.
"""
G1 = input()
G2 = input()
G1 = G1[::-1]  # G1은 뒤집기
G1_drt = {ch: 1 for ch in G1}  # G1의 방향벡터
G2_drt = {ch: -1 for ch in G2}  # G2의 방향벡터

ants = list(G1 + G2)
T = int(input())
for _ in range(T):
    # 여기서부터 개미 시뮬레이션 시작

    is_seen1 = False
    exchange = []
    for idx, ant in enumerate(ants) :
        if G1_drt.get(ant, 0):
            dx = G1_drt[ant]
        elif G2_drt.get(ant, 0):
            dx = G2_drt[ant]

        if dx == 1 :
            is_seen1 = True
        if dx == -1 and is_seen1 :
            exchange.append([idx-1, idx])
            is_seen1 = False

    for t1, t2 in exchange :
        ants[t1], ants[t2] = ants[t2], ants[t1]


print(''.join(ants))