def solution(k, m, score):
    # 1. 점수를 내림차순으로 정렬
    score.sort(reverse=True)
    
    # 2. 최대 이익을 계산
    max_profit = 0
    for i in range(0, len(score) - m + 1, m):
        # 그룹의 최저 점수는 i + m - 1번째 사과의 점수
        min_score_in_box = score[i + m - 1]
        max_profit += min_score_in_box * m
    
    return max_profit
