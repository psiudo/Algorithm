import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
ans = [0] * N  # 각 탑에서 수신하는 탑의 번호 (1-indexed)

for i in range(N):
    j = i - 1  # 바로 왼쪽 탑부터 검사
    # 현재 탑보다 작거나 같은 탑은 점프로 건너뛰기
    while j >= 0 and towers[j] <= towers[i]:
        # ans[j]는 1-indexed이므로, 0-indexed로 만들기 위해 -1
        j = ans[j] - 1  
    # j가 유효하면 j+1이 답, 아니면 0
    if j >= 0:
        ans[i] = j + 1
    else:
        ans[i] = 0

print(" ".join(map(str, ans)))
