attendance = [0]*30

for i in range(28) :
    j = int(input())
    attendance[j-1] += 1

for i in range(30) :
    if attendance[i] == 0 :
        print(i+1)