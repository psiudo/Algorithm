N = int(input())
reminder = N % 15
quotient = N // 15
result = -1

if quotient < 1 :
    if N % 3 == 0 :
        result = N // 3
    elif N % 5 == 0 :
        result = N // 5
    elif N == 8 :
        result = 2
    elif N == 11 :
        result = 3
    elif N == 13 :
        result = 3
    elif N == 14 :
        result = 4


if quotient >= 1 :
    if reminder == 1:
        quotient -= 1
        result = quotient * 3 + 4
    elif reminder == 2 :
        quotient -= 1
        result = quotient * 3 + 5
    elif reminder % 3 == 0 :
        result = quotient * 3 + reminder//3
    elif reminder == 4 :
        quotient -= 1
        result = quotient * 3 + 5
    elif reminder % 5 == 0 :
        result = quotient * 3 + reminder//5
    elif reminder == 7 :
        quotient -= 1
        result = quotient * 3 + 6
    elif reminder == 8 :
        result = quotient * 3 + 2
    elif reminder == 11 :
        result = quotient * 3 + 3
    elif reminder == 13:
        result = quotient * 3 + 3
    elif reminder == 14 :
        result = quotient * 3 + 4

if N % 5  == 0:
    result = N // 5

print(result)