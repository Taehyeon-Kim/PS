'''
순서가 주어져있는 문제 - 시키는대로 하면 됨

커맨드
1. 배열 슬라이싱
2. 오름차순 정렬
3. k번째 숫자 인덱스로 접근
'''


def solution(array, commands):
    answer = []

    # 커맨드가 핵심
    for command in commands:
        temp = array[command[0] - 1: command[1]]
        temp.sort()
        answer.append(temp[command[2] - 1])

    return answer
