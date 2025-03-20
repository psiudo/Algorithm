import sys
from collections import deque

input = sys.stdin.readline
T = int(input())

for ts in range(T) :
    size = int(input())
    start = list(map(int, input().split()))
    final = list(map(int, input().split()))
    
    board = [[0]*size for _ in range(size)]
    visited = [False]*(size**2)
    cnt = 0
    queue = deque([(start[0], start[1], cnt)])
    visited[size*start[1] + start[0]] = True
    
    while queue :
        x, y, cnt = queue.popleft()
        if x == final[0] and y == final[1] :
            print(cnt)
            break

        cnt += 1
        for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)] :
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x <= size - 1 and 0 <= next_y <= size - 1 and not visited[next_y*size + next_x ] : 
                queue.append((next_x, next_y, cnt))
                visited[next_y*size + next_x ] = True