import sys

# 입력 받기
N = int(sys.stdin.readline().strip())
video = [list(sys.stdin.readline().strip()) for _ in range(N)]

def quad_tree(x, y, size):
    """쿼드 트리를 재귀적으로 압축"""
    # 첫 번째 값 저장
    first = video[x][y]
    
    # 전체 영역이 같은 값인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if video[i][j] != first:
                # 4개로 분할
                half = size // 2
                return "(" + quad_tree(x, y, half) + quad_tree(x, y + half, half) + \
                             quad_tree(x + half, y, half) + quad_tree(x + half, y + half, half) + ")"
    
    # 모두 같은 값이라면 해당 값 반환
    return first

# 결과 출력
print(quad_tree(0, 0, N))
