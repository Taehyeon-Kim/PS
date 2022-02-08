import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] += 1

    while q:
        x = q.popleft()
        for city in graph[x]:
            if visited[city] == -1:
                visited[city] = visited[x] + 1
                q.append(city)


n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [-1] * (n+1)
cities = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)
# print(visited)

for i in range(1, n+1):
    if visited[i] == k:
        cities.append(i)

if cities:
    for city in cities:
        print(city)
else:
    print(-1)
