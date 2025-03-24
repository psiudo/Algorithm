import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def w(a, b, c):
    # 기저 조건: a, b, c 중 하나라도 0 이하이면 결과는 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    # a, b, c가 20을 초과하면 w(20, 20, 20)로 치환
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    # 조건: a < b < c인 경우
    if a < b < c:
        return w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    # 그 외의 경우
    return w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)

while True:
    # 한 줄씩 읽어서 처리합니다.
    line = sys.stdin.readline().strip()
    if not line:
        break  # 파일의 끝에 도달한 경우
    a, b, c = map(int, line.split())
    # 종료 조건: -1 -1 -1이면 반복 종료
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")
