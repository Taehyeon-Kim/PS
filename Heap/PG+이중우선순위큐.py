'''
- 힙을 최소힙, 최대힙을 2가지 만들어서 사용하는 방법
- 이 때 하나의 힙에서 pop이 발생했다면, 다른 힙에서도 원소를 제거해주어야 함.

- heapq의 또 다른 메서드인 nlargest 메서드 이용
'''
import heapq


def solution(operations):
    answer = []
    minq = []
    maxq = []

    for operation in operations:
        o, d = operation.split(" ")
        if o == 'I':
            heapq.heappush(minq, int(d))
            heapq.heappush(maxq, -int(d))

        elif o == 'D':
            if len(minq) == 0:
                continue

            if int(d) == 1:
                maxVal = -heapq.heappop(maxq)
                minq.remove(maxVal)
            if int(d) == -1:
                minVal = heapq.heappop(minq)
                maxq.remove(-minVal)
    return [0, 0] if len(minq) == 0 else [-heapq.heappop(maxq), heapq.heappop(minq)]
