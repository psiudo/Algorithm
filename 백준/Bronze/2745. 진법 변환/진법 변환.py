B, N = map(str, input().split())
N = int(N)

original_num = reversed(list(B))

cnt = 0
sum = 0

for i in original_num :
    if '0' <= i <= '9' :
        num = int(i)
    else :
        num = (ord(i) - ord('A') + 10)
    sum += num * (N ** cnt)
    cnt += 1


print(sum)