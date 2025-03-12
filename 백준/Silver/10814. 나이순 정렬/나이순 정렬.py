import sys
input = sys.stdin.readline
N = int(input())
users = []
for i in range(N):
    age, name = input().split()
    users.append((int(age), i, name))
users.sort(key=lambda x: (x[0], x[1]))
for age, _, name in users:
    sys.stdout.write(f"{age} {name}\n")
    