import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))

queue_deque = deque()
for i in range(N):
    if A[i] == 0:
        queue_deque.append(B[i])

result = []
if not queue_deque:
    result = C
else:
    for x in C:
        out_val = queue_deque.pop()
        result.append(out_val)
        queue_deque.appendleft(x)

print(" ".join(map(str, result)))
