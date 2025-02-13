T = int(input())


for _ in range(T) :

    ps = input()
    stack_num = 0

    for str in ps :
        if str == '(' :
            stack_num += 1
        elif str == ')' :
            stack_num -= 1

        if stack_num < 0 :
            print('NO')
            break

    else :
        if stack_num == 0 :
            print('YES')
        else :
            print('NO')



