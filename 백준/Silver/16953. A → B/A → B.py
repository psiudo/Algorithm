a,b = map(int, input().split())
answer = 1

while b > a:
    if b % 10 == 1:
        b //= 10
        answer += 1
    elif b % 2 == 0:
        b //= 2
        answer += 1
    else:
        print(-1)
        break
else:
    print(answer if b == a else -1)