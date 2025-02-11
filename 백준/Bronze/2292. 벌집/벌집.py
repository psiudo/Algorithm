N = int(input())

circle = 1
i = 0

while circle < N :
   circle += 6*i
   i += 1

if i == 0 :
    i = 1
print(i)