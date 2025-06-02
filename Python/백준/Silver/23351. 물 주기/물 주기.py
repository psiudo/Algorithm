import sys

def first_dead_day(N, K, A, B):
    q = N // A          # 같은 화분이 다시 물을 받기까지 주기
    r = q - 1           # 첫 물까지 기다리는 최대 일수

    if K <= r:          # 첫 물을 받기 전에 바로 죽음
        return K

    M0 = K - q + B      # 첫 물을 받은 날이 끝난 뒤 수분
    D  = q - B          # 주기마다 순감소량  D>0

    if M0 <= r:
        k = 0
    else:
        k = (M0 - r + D - 1) // D   # 정수형 올림

    M  = M0 - k * D                 # 마지막으로 물을 받은 날 끝 수분
    return (r + 1) + k * q + M      # 사망한 날짜

if __name__ == "__main__":
    N, K, A, B = map(int, sys.stdin.readline().split())
    print(first_dead_day(N, K, A, B))
