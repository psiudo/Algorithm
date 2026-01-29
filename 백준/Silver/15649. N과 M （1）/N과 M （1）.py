import sys
N, M = map(int, input().split())
result = [] 

all_mask = (1 << N) - 1 # 0번 ~ (N-1)번 비트가 켜진 마스크

def solve(depth, visited_mask):
    if depth == M:
        print(*result)
        return

    available = all_mask & ~visited_mask

    while available:
        pos = available & -available 
        available -= pos
        i = pos.bit_length()
        result.append(i)
        solve(depth + 1, visited_mask | pos)
        result.pop() 

solve(0, 0)