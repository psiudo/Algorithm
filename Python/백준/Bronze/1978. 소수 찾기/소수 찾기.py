N = int(input())
num_list = list(map(int, input().split()))
cnt =0 
for num in num_list :
    if num == 1 : 
        continue

    for i in range(2, num//2 + 1) :
        if num%i == 0 :
            break
    else :
        cnt += 1

print(cnt)
