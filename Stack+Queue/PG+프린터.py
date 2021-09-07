'''
차분하게 큐의 성질을 이용해서 풀면 되는 문제

Check Point
- enumerate()
- check 변수
'''


def solution(priorities, location):
    queue = []
    printer = []
    for (idx, pr) in enumerate(priorities):
        queue.append((pr, idx))

    while queue:
        check = False
        popElement = queue.pop(0)
        for docs in queue:
            if popElement[0] < docs[0]:
                check = True

        if check:
            queue.append(popElement)
        else:
            printer.append(popElement)

    for i in range(len(printer)):
        if printer[i][1] == location:
            return i + 1
