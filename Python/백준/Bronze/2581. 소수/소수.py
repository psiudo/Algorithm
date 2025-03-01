M = int(input())
if M == 1 :
    M = 2
N = int(input())
num_list = list(range(M, N+1))

for i in range(2 , int(N**0.5)+1) :
    start = max(i*i, ((M+i-1)//i)*i)
    for j in range(start, N+1, i) :
        if j in num_list :
            num_list.remove(j)


if len(num_list) == 0 : 
    print('-1')
else :    
    print(sum(num_list))
    print(min(num_list))