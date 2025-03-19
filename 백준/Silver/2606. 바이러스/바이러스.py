from collections import deque

numComputers= int(input())
numConnections = int(input())
network = [[] for i in range(numComputers+1)]

for _ in range(numConnections) :
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

VisitedAndOrder = [0]*(numComputers+1)
dq = deque()
dq.append(1)
order = 1
VisitedAndOrder[1] = order
while dq :
    cur = dq.popleft()

    for i in network[cur] :
        if VisitedAndOrder[i] == 0 :
            order += 1
            VisitedAndOrder[i] = order
            dq.append(i)

print(numComputers - VisitedAndOrder.count(0))