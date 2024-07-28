def solution(arr):
    if not arr:
        return []

    result = [arr[0]]  # 첫 번째 원소는 항상 포함

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])

    return result
