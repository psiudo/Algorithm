from collections import Counter

def solution(participant, completion):
    # Counter 객체를 이용해 차를 구하고, 남아있는 키를 반환
    result = Counter(participant) - Counter(completion)
    return list(result.keys())[0]
