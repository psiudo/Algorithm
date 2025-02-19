
N = int(input())
sangeun = sorted(list(map(int, input().split())))

M = int(input())
num_card = list(map(int, input().split()))


def binary_search(arr, target, left, right):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


for i in range(M):
    k = binary_search(sangeun, num_card[i], 0, N - 1)
    if num_card[i] == sangeun[k] :
        print('1', end=' ')
    elif k == -1:
        print('0', end=' ')
