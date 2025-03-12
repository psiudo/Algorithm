def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1] or (left[i][1] == right[j][1] and left[i][0] < right[j][0]):
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    while i < len(left):
        sorted_arr.append(left[i])
        i += 1

    while j < len(right):
        sorted_arr.append(right[j])
        j += 1

    return sorted_arr

N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_points = merge_sort(points)

for x, y in sorted_points:
    print(x, y)
