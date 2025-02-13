import sys


K = int(sys.stdin.readline())
stack_list = []

for i in range(K) :
    num = int(sys.stdin.readline())
    if num == 0 :
        stack_list.pop()
    else :
        stack_list.append(num)

print(sum(stack_list))