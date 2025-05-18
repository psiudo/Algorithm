import sys
from collections import defaultdict

N, M = map(int, input().split())
trees = sorted(list(map(int, input().split())))
sum_list = defaultdict(list)

def search_height() :
    left = 0
    right = trees[-1]
    mid = ( left + right ) // 2
    
    while left <= right :
        mid = ( left + right ) // 2
        sum = 0
        for h in trees :
            if h > mid :
                sum += h - mid
        
        
        if sum >= M :
            left = mid + 1
            sum_list[mid].append(sum)
        else :
            right = mid - 1

    return

search_height()

ans = max(sum_list) if sum_list else 0
print(ans)