from collections import deque


def dfs(start):
    print(start, end=' ')
    visited[start] = True
    for i in graph[start]:
        if visited[i] is False:
            dfs(i)


def bfs(start):
    # 시작점
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if visited[i] is False:
                queue.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 인접리스트 생성
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# 인접리스트 정렬
for i in range(1, n+1):
    graph[i].sort()

dfs(v)
print()
visited = [False] * (n + 1)  # 방문 리스트 초기화
bfs(v)
