import heapq
import sys

input = sys.stdin.readline
N = int(input())

hq = []
for _ in range(N) :
    x = int(input())
    if x != 0 :
        heapq.heappush(hq, -x)
    else :
        if not hq :
            print(0)
        else :
            temp = heapq.heappop(hq)
            print(-temp)