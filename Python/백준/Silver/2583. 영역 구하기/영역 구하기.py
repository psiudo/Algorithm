def find_areas(M, N, rectangles):
    # 모눈종이 초기화
    grid = [[0] * N for _ in range(M)]
    
    # 직사각형 그리기
    for x1, y1, x2, y2 in rectangles:
        for i in range(y1, y2):
            for j in range(x1, x2):
                grid[i][j] = 1

    # DFS를 통한 영역 탐색
    def dfs(x, y):
        stack = [(x, y)]
        area = 0
        while stack:
            cx, cy = stack.pop()
            if cx < 0 or cy < 0 or cx >= M or cy >= N or grid[cx][cy] == 1:
                continue
            grid[cx][cy] = 1  # 방문 처리
            area += 1
            stack.append((cx + 1, cy))
            stack.append((cx - 1, cy))
            stack.append((cx, cy + 1))
            stack.append((cx, cy - 1))
        return area

    areas = []
    
    for i in range(M):
        for j in range(N):
            if grid[i][j] == 0:
                area = dfs(i, j)
                areas.append(area)
    
    areas.sort()
    return len(areas), areas

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

M, N, K = int(data[0]), int(data[1]), int(data[2])
rectangles = [(int(data[i*4+3]), int(data[i*4+4]), int(data[i*4+5]), int(data[i*4+6])) for i in range(K)]

# 영역 구하기
num_areas, areas = find_areas(M, N, rectangles)

# 결과 출력
print(num_areas)
print(" ".join(map(str, areas)))
