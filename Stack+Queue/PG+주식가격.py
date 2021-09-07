'''
그냥 완탐으로 풀 수 있을 것 같은 문제 (실제로 그랬다.)
이게 근데 왜 스택/큐 문제인지 모르겠네
'''


def solution(prices):
    answer = []
    length = len(prices)

    for i in range(length):
        time = 0
        for j in range(i+1, length):
            if prices[i] > prices[j]:
                time += 1
                break
            time += 1
        answer.append(time)
    return answer
