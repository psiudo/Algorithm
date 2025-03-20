
import sys
from collections import deque

T = int(input())

for ts in range(T) :
    size = int(input())
    start = list(map(int, input().split()))
    final = list(map(int, input().split()))
    
    board = [[0]*size for _ in range(size)]
    visited = [-1]*(size**2)
    queue = deque([[start[0], start[1]]])
    visited[size*start[1] + start[0]] = 0
    
    while queue :
        x, y = queue.popleft()
        if x == final[0] and y == final[1] :
            print(visited[y*size + x])
            break
        for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)] :
            next_x, next_y = x + dx, y + dy
            if 0 <= next_x <= size - 1 and 0 <= next_y <= size - 1 and visited[next_y*size + next_x ] < 0 : 
                queue.append([next_x, next_y])
                visited[next_y*size + next_x ] = visited[y*size + x] + 1