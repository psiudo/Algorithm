import math
X = int(input().strip())
d = int(-(-((math.sqrt(8 * X + 1) - 1) / 2) // 1))
prev = (d - 1) * d // 2
k = X - prev
if d % 2 == 0:
    numerator = int(k)
    denominator = int(d + 1 - k)
else:
    numerator = int(d + 1 - k)
    denominator = int(k)
print(f"{numerator}/{denominator}")
