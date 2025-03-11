import sys

class CircularQueue:
    def __init__(self, capacity=2000001):
        self.queue = [0] * capacity
        self.capacity = capacity
        self.f = 0
        self.r = 0
        self.count = 0

    def push(self, x):
        if self.count == self.capacity - 1:
            return
        self.queue[self.r] = x
        self.r = (self.r + 1) % self.capacity
        self.count += 1

    def pop(self):
        if self.count == 0:
            return "-1"
        val = self.queue[self.f]
        self.f = (self.f + 1) % self.capacity
        self.count -= 1
        return str(val)

    def size(self):
        return str(self.count)

    def empty(self):
        return "1" if self.count == 0 else "0"

    def front(self):
        return str(self.queue[self.f]) if self.count > 0 else "-1"

    def back(self):
        return str(self.queue[(self.r - 1) % self.capacity]) if self.count > 0 else "-1"

def process_queue():
    queue = CircularQueue()
    output = []
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        command = sys.stdin.readline().strip().split()
        op = command[0]
        if op == "push":
            queue.push(int(command[1]))
        elif op == "pop":
            output.append(queue.pop())
        elif op == "size":
            output.append(queue.size())
        elif op == "empty":
            output.append(queue.empty())
        elif op == "front":
            output.append(queue.front())
        elif op == "back":
            output.append(queue.back())
    sys.stdout.write("\n".join(output) + "\n")

process_queue()
