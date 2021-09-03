'''
Python으로 구현한 BFS Base 코드
- 가장 기본적인 틀은 언제든지 사용할 수 있게 암기가 되어야 한다.
'''

from collections import deque       # 큐를 구현하기 위해 deque 사용


def bfs(graph, start, visited):     # bfs 함수
    queue = deque([start])          # 시작점을 큐에 넣고 시작
    visited[start] = True           # 시작점에 대한 방문 처리 *

    while queue:                    # 큐가 빌 때까지 반복
        v = queue.popleft()         # 큐에서 원소 하나 꺼내기

        for i in graph[v]:          # 꺼낸 원소에 대해 상하좌우를 살펴보기 위함
            if not visited[i]:      # 방문하지 않았다면
                visited[i] = True   # 방문처리하고
                queue.append(i)     # 큐에 원소 추가


# 연결리스트
graph = [
    [],
    [2, 3],
    [1],
    [3, 6],
    [1, 2, 6],
    [6],
    [2, 5],
]

# 방문 표시할 배열
visited = [False] * 7

# bfs 실행
bfs(graph, 1, visited)
