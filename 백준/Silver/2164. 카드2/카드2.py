import sys

def process():
    n = int(sys.stdin.readline().strip())
    queue = list(range(1, n + 1))
    front = 0

    while len(queue) - front > 1:
        front += 1
        queue.append(queue[front])
        front += 1

    print(queue[front])

process()
