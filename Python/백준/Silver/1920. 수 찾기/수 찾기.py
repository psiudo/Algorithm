N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
nums = list(map(int, input().split()))

def bin_search(number) :
    left, right = 0, len(A)-1
    while left <= right :
        mid = (left + right) // 2
        if A[mid] > number :
            right = mid - 1
        elif A[mid] < number :
            left = mid + 1 
        elif A[mid] == number :
            return 1
    return 0

for number in nums :
    result = bin_search(number)
    print(result)