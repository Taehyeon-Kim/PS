# boj 11724 연결 요소의 개수
# 기본 뼈대 문제 - bfs, dfs
# bfs 풀이 시간초과 : input = sys.stdin.readline로 해결

from collections import deque
import sys
input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

cnt = 0
for i in range(1, n+1):
    if visited[i] is False:
        bfs(i)
        cnt += 1
print(cnt)
