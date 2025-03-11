import sys

class StackQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return str(self.out_stack.pop()) if self.out_stack else "-1"

    def size(self):
        return str(len(self.in_stack) + len(self.out_stack))

    def empty(self):
        return "1" if not (self.in_stack or self.out_stack) else "0"

    def front(self):
        if self.out_stack:
            return str(self.out_stack[-1])
        elif self.in_stack:
            return str(self.in_stack[0])
        return "-1"

    def back(self):
        if self.in_stack:
            return str(self.in_stack[-1])
        elif self.out_stack:
            return str(self.out_stack[0])
        return "-1"

input = sys.stdin.readline
output = sys.stdout.write

N = int(input().strip())
queue = StackQueue()
result = []

for _ in range(N):
    cmd = input().strip().split()
    if cmd[0] == "push":
        queue.push(int(cmd[1]))
    elif cmd[0] == "pop":
        result.append(queue.pop() + "\n")
    elif cmd[0] == "size":
        result.append(queue.size() + "\n")
    elif cmd[0] == "empty":
        result.append(queue.empty() + "\n")
    elif cmd[0] == "front":
        result.append(queue.front() + "\n")
    elif cmd[0] == "back":
        result.append(queue.back() + "\n")

output("".join(result))