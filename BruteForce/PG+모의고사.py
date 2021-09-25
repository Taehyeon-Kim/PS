'''
1번: 12345 ...
2번: 21232425 ...
3번: 3311224455 ...

완탐?

정답배열과 각각의 사람의 답안 배열을 비교하는 방식
카운트배열도 필요해 가장 많이 맞춘 사람을 출력해야하니까 -> 딕셔너리로 만들면 편할듯 -> 아니면 3명밖에 없으니까 각각 변수 생성

1. 배열을 문제개수만큼 늘려줘야함
2. 각 배열을 비교하는 작업
'''


def solution(answers):
    answer = []
    questionCount = len(answers)
    first = [1, 2, 3, 4, 5] * questionCount
    second = [2, 1, 2, 3, 2, 4, 2, 5] * questionCount
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * questionCount

    countDict = {'1': 0, '2': 0, '3': 0}

    for i in range(questionCount):
        if first[i] == answers[i]:
            countDict['1'] += 1
        if second[i] == answers[i]:
            countDict['2'] += 1
        if third[i] == answers[i]:
            countDict['3'] += 1

    for item in countDict.items():
        if item[1] == max(countDict['1'], countDict['2'], countDict['3']):
            answer.append(int(item[0]))

    return answer
