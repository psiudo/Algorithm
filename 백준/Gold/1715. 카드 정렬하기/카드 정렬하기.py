
"""
10만 => 순열?? == 멸망
1) 큰 애들은 나중에 합치자. 큰 애들 미뤄야 한다.
2) 계속 작은 카드를 만들고 작은 카드와 작은 카드를 더하자. (그리디한 접근)
3) 최솟값과 그 다음값을 합치고 이 결과가 최소인지 확인하려면 매번 정렬해야한다.
4) 매번 정렬하는 건 많은 비용이 든다.
"""
import heapq

N = int(input())
cards = []
for _ in range(N) :
    cards.append(int(input()))
heapq.heapify(cards)
# print(cards) [10, 20, 40]
# ==========================================
tot_cal = 0
for _ in range(N-1) : # 2개가 하나로 합쳐지니까 매 루프당 -1씩 카드가 없어진다. 즉, N-1번만 시행하면 된다.
    min1 = heapq.heappop(cards)
    min2 = heapq.heappop(cards)
    tot_cal += min1 + min2 # 연산량을 더해준다.
    heapq.heappush(cards, min1+min2) # 새로운 카드 뭉치가 만들어진다.

print(tot_cal)