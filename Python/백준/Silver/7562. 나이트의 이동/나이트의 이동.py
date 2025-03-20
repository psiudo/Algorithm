from collections import deque
import sys
input = sys.stdin.read

# 나이트의 8가지 이동 방향
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

def bfs_knight(l, start, end):
    if start == end:
        return 0

    queue = deque([start])
    visited = [[False] * l for _ in range(l)]
    visited[start[0]][start[1]] = True
    distance = [[0] * l for _ in range(l)]

    while queue:
        x, y = queue.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy

            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))

                if (nx, ny) == end:
                    return distance[nx][ny]

    return -1  # 도달 불가능한 경우 (문제 조건상 발생하지 않음)

def main():
    data = input().split()
    T = int(data[0])
    index = 1
    results = []

    for _ in range(T):
        l = int(data[index])
        start = (int(data[index + 1]), int(data[index + 2]))
        end = (int(data[index + 3]), int(data[index + 4]))
        index += 5

        result = bfs_knight(l, start, end)
        results.append(result)

    for res in results:
        print(res)

if __name__ == "__main__":
    main()
