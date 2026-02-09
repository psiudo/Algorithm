"""
1s/1b 
1s/2b
3b
2s
가 유일한 경우
2s/1b는 불가능
3s는 개꿀
zzzzzzzz
1b
1s
까지 하면 됨

그냥 하면 풀린다. 집중해서 하면 풀린다.

"""
N = int(input())
lst = []
for _ in range(N) :
    num, strike, ball = map(int, input().split())
    lst.append((num, strike, ball))

# =====================================================
first_candi = [i for i in range(123, 1000)]
first_candi = set(first_candi)

candi_ans = set()
num_lst = '123456789'
for num, s, b in lst :

    if s == 1 and b == 1 : # 규칙성 있긴 한데 노가다
        candi_full = []
        cnt = 0
        for i in range(9) : # X - ? - Y
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[0] + num_lst[i] + str(num)[1]))
        for i in range(9) : # X - Z - ?
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[0] + str(num)[2] + num_lst[i]))
        for i in range(9) : # ? - Y - X
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(num_lst[i] + str(num)[1] + str(num)[0]))
        for i in range(9) : # Z - Y - ?
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[2] + str(num)[1] + num_lst[i]))
        for i in range(9) : # ? - X - Z
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(num_lst[i] + str(num)[0] + str(num)[2]))
        for i in range(9) : # Y - ? - Z
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[1] + num_lst[i] + str(num)[2] ))

        candi_full = set(candi_full) #############

    elif s == 1 and b == 2 :
        candi_full = []

        candi_full.append(int(str(num)[0] + str(num)[2] + str(num)[1])) # X - Z - Y
        candi_full.append(int(str(num)[2] + str(num)[1] + str(num)[0])) # Z - Y - X
        candi_full.append(int(str(num)[1] + str(num)[0] + str(num)[2])) # Y - X - Z

        candi_full = set(candi_full)  #############

    elif s == 2 :
        candi_full = []

        for i in range(9) : # X - Y - ?
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[0] + str(num)[1] + num_lst[i]))

        for i in range(9) : # X - ? - Z
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(str(num)[0] + num_lst[i] + str(num)[2]))

        for i in range(9) : # ? - Y - Z
            if num_lst[i] in str(num) :
                continue
            candi_full.append(int(num_lst[i] + str(num)[1] + str(num)[2]))

        candi_full = set(candi_full)  #############
    elif s == 0 and b == 2:
        candi_full = set()
        X, Y, Z = str(num)

        for a in num_lst:  # a는 새로운 숫자
            if a in (X, Y, Z):
                continue

            # (missing X) -> {Y,Z}만 ball
            candi_full.add(int(a + Z + Y))  # A Z Y
            candi_full.add(int(Z + a + Y))  # Z A Y
            candi_full.add(int(Y + Z + a))  # Y Z A

            # (missing Y) -> {X,Z}만 ball
            candi_full.add(int(a + Z + X))  # A Z X
            candi_full.add(int(Z + a + X))  # Z A X
            candi_full.add(int(Z + X + a))  # Z X A

            # (missing Z) -> {X,Y}만 ball
            candi_full.add(int(a + X + Y))  # A X Y
            candi_full.add(int(Y + a + X))  # Y A X
            candi_full.add(int(Y + X + a))  # Y X A

        candi_full = set(candi_full)  #############


    elif b == 3 :
        candi_full = []

        candi_full.append(int(str(num)[2] + str(num)[0] + str(num)[1]))  # Z - X - Y
        candi_full.append(int(str(num)[1] + str(num)[2] + str(num)[0]))  # Y - Z - X

        candi_full = set(candi_full)  #############
    elif s == 3 :
        candi_full = []

        candi_full.append(int(str(num)[0] + str(num)[1] + str(num)[2]))  # Z - X - Y
        candi_full = set(candi_full)  #############

    elif s == 1 and b == 0:
        candi_full = []

        for i in range(9) : # X - ? - ?
            for j in range(9) :
                if i == j : continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)) :
                    continue
                candi_full.append(int( str(num)[0] + num_lst[i] + num_lst[j] ))


        for i in range(9) : # ? - Y - ?
            for j in range(9) :
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)) :
                    continue
                candi_full.append(int( num_lst[i] + str(num)[1] + num_lst[j] ))

        for i in range(9) : # ? - ? - Z
            for j in range(9) :
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)) :
                    continue
                candi_full.append(int( num_lst[i] + num_lst[j] + str(num)[2] ))


        candi_full = set(candi_full) #############

    elif s == 0 and b == 1:
        candi_full = []

        for i in range(9):  # ? - X - ?
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int(num_lst[i] + str(num)[0] + num_lst[j]))

        for i in range(9):  # ? - ? - X
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int(num_lst[i] + num_lst[j] + str(num)[0] ))

        for i in range(9):  # Y - ? - ?
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int( str(num)[1] + num_lst[i] + num_lst[j] ))

        for i in range(9):  # ? - ? - Y
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int(num_lst[i] + num_lst[j] + str(num)[1]))

        for i in range(9):  # ? - Z - ?
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int(num_lst[i] + str(num)[2] + num_lst[j] ))

        for i in range(9):  # Z - ? - ?
            for j in range(9):
                if i == j: continue
                if (num_lst[i] in str(num)) or (num_lst[j] in str(num)):
                    continue
                candi_full.append(int( str(num)[2] + num_lst[i] + num_lst[j] ))

        candi_full = set(candi_full)  #############

    elif s == 0 and b == 0 :
        candi_full = []
        for i in range(9) :
            for j in range(9) :
                for k in range(9) :
                    if i == j or i == k or j == k :
                        continue
                    if ( num_lst[i] in str(num) ) or ( num_lst[j] in str(num) ) or ( num_lst[k] in str(num) ) :
                        continue
                    candi_full.append(int( num_lst[i] + num_lst[j] + num_lst[k] ))
        candi_full = set(candi_full)


    first_candi = first_candi & candi_full

print(len(first_candi))


