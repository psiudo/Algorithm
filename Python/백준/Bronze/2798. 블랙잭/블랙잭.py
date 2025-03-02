N, M = map(int, input().split())
card = list(map(int, input().split()))
select = [0]*3
black_jack = -100
for i in range(N-2) :
    select[0] = card[i]
    for j in range(i+1, N-1) :
        select[1] = card[j]
        for k in range(j+1, N) :
            select[2] = card[k]
            temp = sum(select)
            if temp <= M and temp > black_jack :
                black_jack = temp

print(black_jack) 
