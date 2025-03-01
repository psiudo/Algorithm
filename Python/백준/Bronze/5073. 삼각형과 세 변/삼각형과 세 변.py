while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break

    sides = [a, b, c]
    sides.sort()
    # 삼각형 조건: 가장 긴 변 < 나머지 두 변의 합
    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
