import sys
input = sys.stdin.readline
N = int(input())
users = []
for _ in range(N):
    age, name = input().split()
    users.append((int(age), name))
# No explicit index needed because sort is stable
users.sort(key=lambda x: x[0])
for age, name in users:
    sys.stdout.write(f"{age} {name}\n")
