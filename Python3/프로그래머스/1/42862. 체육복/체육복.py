def solution(n, lost, reserve):
    # 여벌 체육복이 있지만 도난당한 경우를 제거
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)
    
    # 여벌 체육복을 빌려줄 수 있는 경우를 확인
    for student in reserve_set:
        if student - 1 in lost_set:
            lost_set.remove(student - 1)
        elif student + 1 in lost_set:
            lost_set.remove(student + 1)
    
    # 체육복을 가지지 못한 학생의 수를 전체 학생 수에서 빼기
    return n - len(lost_set)
