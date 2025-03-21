import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split()) # 차례로 사다리와 뱀
board = {}

for _ in range(N+M) :
    a, b = map(int, input().split())
    board[a] = b

start = 1
cnt = 0
q = deque([(start, cnt)])
visited = [0]*101

def bfs() :
    while q :
        loc, cnt = q.popleft()
        if loc == 100 :
            return cnt

        for i in range(1, 7):
            next = loc + i
            if next in board :
                next = board[next]
            if next <= 100 and visited[next] == 0 :
                visited[next] = 1
                q.append((next, cnt+1))

cnt = bfs()

print(cnt)