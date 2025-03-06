d_minus2 = 0
d_minus1 = 0
d_0 = 1

def fibo(t, a, b, c) :
      if t == n :
          return a+b+c

      return fibo(t+1, b, c, a+b+c)

T = int(input())

for ts in range(T) :
    n = int(input())
    ans = fibo(1, d_minus2, d_minus1, d_0)
    print(ans)
