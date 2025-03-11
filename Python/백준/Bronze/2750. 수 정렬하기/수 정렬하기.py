N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(N-1):
    for j in range(N-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

for num in arr:
    print(num)
