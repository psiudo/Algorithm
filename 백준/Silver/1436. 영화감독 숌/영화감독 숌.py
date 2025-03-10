def where666(exp, k):
    if k % 10 == 6:
        return where666(exp + 1, k // 10)
    else:
        if '666' in str(k) :
            return exp, True
        else:
            return exp, False
        
N = int(input())
cnt = 0
i = 0

while cnt < N:
    exp, has666 = where666(0, i)
    if 0 < exp <= 3:
        for j in range(0, 10 ** exp):
            cnt += 1
            current = int(str(i) + '6' * (3 - exp) + str(j).zfill(exp))

            if N == cnt:
                break

    elif has666 == False :
        cnt += 1
        current = int(str(i) + '666')
        
        if N == cnt:
            break

    elif has666 == True:
        for j in range(0, 10 ** 3):
            current = int(str(i) + str(j).zfill(3))

            if N == cnt:
                break
            cnt += 1

    i += 1
print(current)