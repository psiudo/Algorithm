N = int(input())
inner_num = list(map(int, input().split()))
arr = [[i+1, inner_num[i]] for i in range(N)]

idx, inner = arr.pop(0)
ans = [idx]

if inner > 0:
    k = (inner - 1) % len(arr)
else:
    k = inner % len(arr)

while arr :
    idx, inner = arr.pop(k)
    ans.append(idx)
    
    if not arr :
        break
    
    if inner > 0 :
        k = ( k + inner - 1) % len(arr)
    else :
        k = ( k + inner) % len(arr)

print(" ".join(map(str, ans)))
