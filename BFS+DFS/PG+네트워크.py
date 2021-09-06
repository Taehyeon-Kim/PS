'''
그래프와 트리 모양에서 가장 베이스가 되는 탐색 방법이 BFS, DFS

- 각 노드 간의 거리도 일정하고, 각 노드 간 "연결 여부"만 파악하면 됨
- 이 부분을 각 서브 트리의 개수를 찾는 것이라고 이해할 수도 있을 듯
- 그렇기 때문에 그냥 BFS 또는 DFS를 사용해서 문제를 풀 수 있음

- 함수로 만들어서 bfs나 dfs를 돌리는 것이 나중에 복잡한 문제를 풀 때에도 편할 듯
- 방문 여부를 체크하는 배열 중요
- 개인적으로 True, False보다 0, 1이 더 편함(깔끔하고)
'''

from collections import deque


def bfs(n, graph, start, visited):
    queue = deque([start])
    visited[start] = 1

    while queue:
        v = queue.popleft()
        for i in range(n):
            if not visited[i] and graph[v][i] == 1:
                queue.append(i)
                visited[i] = 1


def solution(n, computers):
    answer = 0
    visited = [0] * n

    for i in range(n):
        if not visited[i]:
            bfs(n, computers, i, visited)
            answer += 1

    return answer
