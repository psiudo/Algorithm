N = int(input())
M = int(input())

parent = [i for i in range(N)]


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        parent[root_b] = root_a


for i in range(N):
    connection = list(map(int, input().split()))
    for j in range(N):
        if connection[j] == 1 and i <= j:
            union(i, j)

plan = list(map(int, input().split()))
plan = [city - 1 for city in plan]

root = find(plan[0])
possible = all(find(city) == root for city in plan)

print("YES" if possible else "NO")