import heapq

'''
job[0] : 시작시간
job[1] : 작업시간

현시점에서 작업이 가능한지를 항상 체크
- 작업중인 다른 작업이 있는지
- 작업 시작가능한 시간인지
'''


def solution(jobs):
    cur, total, i = 0, 0, 0
    start = -1
    h = []

    while i < len(jobs):
        for job in jobs:
            # 작업이 가능한 시간인지 체크
            if start < job[0] <= cur:
                heapq.heappush(h, (job[1], job[0]))

        if len(h) > 0:
            current = heapq.heappop(h)
            start = cur
            cur += current[0]  # 작업시간
            total += (cur - current[1])
            i += 1
        else:
            cur += 1

    return total // len(jobs)
