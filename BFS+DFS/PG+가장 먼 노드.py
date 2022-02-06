from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [-1] * (n+1)

    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # print(graph)

    queue = deque([1])
    dist[1] = 0

    while queue:
        x = queue.popleft()

        for i in graph[x]:
            if dist[i] == -1:
                queue.append(i)
                dist[i] = dist[x] + 1

    for d in dist:
        if d == max(dist):
            answer += 1

    return answer
