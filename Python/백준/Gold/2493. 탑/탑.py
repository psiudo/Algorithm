import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
stack = []
result = [0] * N

for i in range(N):
    # 현재 탑보다 낮은 탑들은 스택에서 제거
    while stack and towers[stack[-1]] < towers[i]:
        stack.pop()
    # 스택이 비어있지 않다면, 스택의 최상단 탑이 현재 탑의 레이저 신호를 수신하는 탑
    result[i] = stack[-1] + 1 if stack else 0
    # 현재 탑 인덱스를 스택에 추가
    stack.append(i)

print(" ".join(map(str, result)))
