import sys
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
sangeun = {} 
for num in map(int, input().split()):
    sangeun[num] = 1 

M = int(input())
num_card = map(int, input().split())


result = []
for num in num_card:
    if num in sangeun:
        result.append("1")
    else:
        result.append("0")

output(" ".join(result) + "\n")
