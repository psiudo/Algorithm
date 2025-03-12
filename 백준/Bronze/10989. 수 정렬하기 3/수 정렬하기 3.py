import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001
for _ in range(N):
    count[int(input())] += 1
for i in range(10001):
    if count[i]:
        s = str(i) + "\n"
        times = count[i]
        while times:
            chunk = min(times, 10000)
            sys.stdout.write(s * chunk)
            times -= chunk
