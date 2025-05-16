import bisect

N = int(input())
num_list = list(map(int, input().split()))

lis = []

for num in num_list:
    idx = bisect.bisect_left(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))
