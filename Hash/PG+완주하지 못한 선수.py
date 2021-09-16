# participant : 모든 선수
# completion : 완료한 선수
# return? -> 완주하지 못한 선수(1명)

# 총 선수는 1 ~ 100,000
# len(completion) = len(participant) - 1
# 참가자 이름
# 동명이인 가능

# 전체 참여자목록에서 완료 선수를 적절하게 잘 비교해서 잘 빼주어야 함.
# 비교라는 키워드
# 어떻게 비교? -> 정렬?

# 정렬 (오름차순으로)
'''
1) 맨 마지막만 남는 경우
eden, kiki, leo
eden, kiki

filipa josipa marina nikola vinko
filipa josipa marina nikola

2) 중간에 나오는 경우
ana mislav mislav stanko
ana mislav stanko

오름차순 정렬 -> 배열 비교 -> 다른 것이 나오는 순간 participant 리턴 또는 마지막 원소 return

10,000,000,000 (백억번의 연산?!)
'''


def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
    else:
        return participant[-1]
    
assert solution(["leo", "kiki", "eden"], ["eden", "kiki"]) == "leo"
assert solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]) == "vinko"
assert solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]) == "mislav"