import sys
import math

def first_dead_day(N, K, A, B):
    q = N // A          # 같은 화분이 물을 받는 간격(일) — 항상 2 ≤ q ≤ 100
    r = q - 1           # 가장 늦게 물을 받는 화분이 첫 물을 기다리는 날수

    # ① 첫 물도 받기 전에 죽는 경우
    if K <= r:          # r일 기다리는 동안 이미 0이 된다
        return K

    # ② 첫 물을 받은 ‘그날’(물 +B, 곧바로 −1) 끝난 뒤의 수분
    M0 = K - r + B - 1

    # 주기마다 순변화(음수)  Δ = B − q   ― 하루 q개 감소, 한 번 +B
    delta = B - q       # 문제 조건 A·B < N ⇒ B < q ⇒ delta < 0

    # ‘물 받은 직후 수분’이 (q-1) 이하가 되면,
    # 다음 물주기까지 q-1일 동안 −1씩 줄어들며 반드시 0에 닿는다.
    thresh = q - 1

    if M0 <= thresh:
        k = 0
    else:
        step = -delta                 # 양수
        k = (M0 - thresh + step - 1) // step   # 정수형 ceil

    Mk = M0 + k * delta   # 마지막으로 물을 받은 날 끝난 뒤의 수분 (1 ≤ Mk ≤ q-1)

    # Mk일 더 지나면 0이 되어 사망
    return (r + 1) + k * q + Mk


if __name__ == "__main__":
    N, K, A, B = map(int, sys.stdin.readline().split())
    print(first_dead_day(N, K, A, B))
