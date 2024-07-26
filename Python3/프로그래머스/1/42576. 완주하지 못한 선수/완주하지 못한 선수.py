from collections import Counter

def solution(participant, completion):
    # 참가자와 완주자의 카운트를 셈
    participant_count = Counter(participant)
    completion_count = Counter(completion)

    # 완주자 수를 참가자 수에서 뺀다
    for name in participant_count:
        if participant_count[name] != completion_count[name]:
            return name
