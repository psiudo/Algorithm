import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, counter, order, graph):
    order[v] = counter[0]
    for u in graph[v]:
        if order[u] == 0:
            counter[0] += 1
            dfs(u, counter, order, graph)

def solve():
    N, M, R = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    order = [0] * (N + 1)

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for i in range(1, N + 1):
        graph[i].sort()

    counter = [1]  # mutable 객체로 선언
    dfs(R, counter, order, graph)
    print("\n".join(map(str, order[1:])))

if __name__ == '__main__':
    solve()
