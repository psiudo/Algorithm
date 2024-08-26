import math
from itertools import combinations

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_of_three(a, b, c):
    return lcm(lcm(a, b), c)

def find_smallest_multiple(nums):
    min_lcm = float('inf')
    for comb in combinations(nums, 3):
        current_lcm = lcm_of_three(*comb)
        count = sum(1 for num in nums if current_lcm % num == 0)
        if count >= 3:
            min_lcm = min(min_lcm, current_lcm)
    return min_lcm

# 입력 부분
nums = list(map(int, input().split()))

# 결과 출력
print(find_smallest_multiple(nums))
