import sys  # bfs
from collections import deque
input = sys.stdin.readline
m, n, h = map(int,input().split()) #n=행 m=열
dy,dx, dz=[-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1] #상하좌우 이동
graph = []

for j in range(h):
    pan= []
    for i in range(n):
        pan.append(list(map(int,input().split()))) #int 반복문 사용시 append를 사용
    graph.append(pan) #subscriptable을 해결하기 위해 입력을 따로 받기

def bfs() :
    q = deque()
    for a in range(h):
        for b in range(n):
            for c in range(m):
                if graph[a][b][c] == 1 : #1인 값들 전부를 q에 넣기
                    q.append((a,b,c))
    while q:
        z, y, x = q.popleft()
        for i in range(6):
            nx, ny , nz= x +dx[i] , y + dy[i], z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            elif graph[nz][ny][nx]==0:
                graph[nz][ny][nx] = graph[z][y][x]+ 1 #기존 토마토값에 +1
                q.append((nz,ny,nx)) #q에 이동한 토마토 위치 넣어줌

bfs() #bfs 호출 graph에 각 값 넣기
ans = 0
for i in graph:
    for j in i:
        for tomato in j:
            if tomato == 0: #그래프안에 0이 있다면 -1출력후 종료
                print(-1)
                exit(0)
        ans = max(ans, max(j))
print(ans -1 ) #처음 시작이 1이기때문에 -1 
