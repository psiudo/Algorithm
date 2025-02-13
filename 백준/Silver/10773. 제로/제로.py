K = int(input())
stack_list = []

for i in range(K) :
    num = int(input())
    if num == 0 :
        stack_list.pop()
    else :
        stack_list.append(num)

print(sum(stack_list))