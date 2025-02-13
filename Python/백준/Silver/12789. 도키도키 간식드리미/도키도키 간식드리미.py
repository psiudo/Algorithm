N = int(input())
current = list(map(int, input().split()))
current = current[::-1]
middle_place = []
k = 1
while current or middle_place :
    if current and current[-1] == k :
        current.pop()
        k += 1
    elif middle_place and middle_place[-1] == k :
        middle_place.pop()
        k += 1
    elif current :
        middle_place.append(current.pop())
    else :
        print("Sad")
        break
else :
    print("Nice")

