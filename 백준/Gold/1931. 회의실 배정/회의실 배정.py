N = int(input())
time_tables = []
for _ in range(N) :
    time_tables.append( tuple(map(int, input().split())) )
time_tables.sort( key = lambda x : (x[1], x[0]) ) # 종료시간 별로 오름차순 정렬
# 엣지케이스1 ) N = 1 일 때 무사 통과
# 엣지케이스2 ) 시작과 동시에 종료되는 회의가 있다고 하자.
"""
만약 종료시간만 정렬해서 time_tables가 
(a, a)
(a-2, a) 
순으로 정렬된다면
a-2, a가 선택될 경우가 사라진다. 따라서, s == e 조건 하에서는 시작시간 별로도 정렬해야 옳다.
"""

prev_end = 0
ans = 0
for curr_start, curr_end in time_tables :
    if prev_end <= curr_start : # 이전 종료시간이 현재 보고 있는 회의의 시작시간보다 이전이라면
        prev_end = curr_end # 그리디하게 현재 회의를 선택
        ans += 1

print(ans)


