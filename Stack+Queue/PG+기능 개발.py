'''
days라는 변수로 컨트롤 해준다는 생각
'''


def solution(progresses, speeds):
    answer = []
    days = 0
    count = 0

    while len(progresses):
        if progresses[0] + days * speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            days += 1
    # 마지막에도 카운트를 추가해주어야 함
    answer.append(count)

    return answer
