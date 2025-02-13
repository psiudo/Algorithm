import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        return self.items.pop() if self.items else -1

    def size(self):
        return len(self.items)

    def empty(self):
        return 0 if self.items else 1

    def top(self):
        return self.items[-1] if self.items else -1


def main():
    input = sys.stdin.readline
    n = int(input().strip())
    stack = Stack()
    output = []

    for _ in range(n):
        command = input().split()
        if command[0] == '1':
            stack.push(command[1])
        elif command[0] == '2':
            output.append(str(stack.pop()))
        elif command[0] == '3':
            output.append(str(stack.size()))
        elif command[0] == '4':
            output.append(str(stack.empty()))
        elif command[0] == '5':
            output.append(str(stack.top()))

    sys.stdout.write("\n".join(output))


if __name__ == '__main__':
    main()
