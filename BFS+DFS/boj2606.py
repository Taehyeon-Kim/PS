# - 날짜 : 21.01.02
# - 작성자 : 김태현
# - BOJ 2606 바이러스
# - BFS, DFS

# Check List
# [x] 스스로 해결한 문제
# [x] But 확실치 않은..
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제

# Count를 왜 -1부터 했을까.. 사실 0부터 시작했을 때 +1 만큼 나오길래 ...
# 다시 한 번 이해해보기

from collections import deque


def bfs(start):
    global count
    q = deque([start])
    visited[start] = True

    while q:
        v = q.popleft()
        count += 1
        for i in graph[v]:
            if visited[i] is False:
                q.append(i)
                visited[i] = True


n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = -1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

bfs(1)
print(count)
