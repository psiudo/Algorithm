import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a
        return True  # 연결됨
    return False  # 사이클

n = int(input())  
m = int(input()) 

parent = [i for i in range(n + 1)]

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

total = 0
for cost, a, b in edges:
    if union(a, b):
        total += cost

print(total)
