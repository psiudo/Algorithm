def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if len(arr[j]) < len(pivot) or (len(arr[j]) == len(pivot) and arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

N = int(input())
words = []
seen = set()

for _ in range(N):
    word = input().strip()
    if word not in seen:
        seen.add(word)
        words.append(word)

quick_sort(words, 0, len(words) - 1)

for word in words:
    print(word)
