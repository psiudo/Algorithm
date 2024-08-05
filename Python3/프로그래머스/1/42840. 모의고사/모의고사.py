def solution(answers):
    # 각 수포자의 찍는 패턴
    patterns = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    # 수포자들의 점수를 저장할 리스트
    scores = [0, 0, 0]
    
    # 정답을 비교하여 점수 계산
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i % len(pattern)]:
                scores[j] += 1
    
    # 최대 점수 계산 및 결과 리스트 작성
    max_score = max(scores)
    result = [i + 1 for i, score in enumerate(scores) if score == max_score]
    
    return result
