
N = int(input())
num_cards = sorted(list(map(int, input().split()))) # 정렬 필수!!!
M = int(input())
candis = list(map(int, input().split()))
length = len(num_cards) - 1
def binary_s(candi) :
    l, m, r = 0, ( 0 + length )//2, length
    while l <= r :
        m = (l+r)//2
        # 찾았다면
        if num_cards[m] == candi :
            return 1
        # 오른쪽에 있다면
        if num_cards[m] < candi :
            l = m + 1
        # 왼쪽에 있다면
        else :
            r = m - 1
    return 0


ans = []
for candi in candis :
    ans.extend([binary_s(candi)])

print(*ans)