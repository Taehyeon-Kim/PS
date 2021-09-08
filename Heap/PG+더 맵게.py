'''
1) 일반 완전탐색으로 푸는 경우
시간복잡도가 좋지 않음

2) heapq를 이용해서 풀어야 함 (우선순위큐와 비슷한 개념)
'''

import heapq


def solution(scoville, K):
    answer = 0
    # 최소 힙으로 변환
    heapq.heapify(scoville)

    while len(scoville) > 1:

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)

        answer += 1

        if scoville[0] >= K:
            return answer

    return -1
