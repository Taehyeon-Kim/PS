# - 날짜 : 21.01.04
# - 작성자 : 김태현
# - BOJ 1012 유기농 배추
# - BFS, DFS

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제

# 행과 열의 방향을 잘 파악하는게 중요했던 문제 (중요한 포인트*)
# 테스트 케이스가 여러 개 들어온 문제

from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                queue.append((nx, ny))
                graph[nx][ny] = 0


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

t = int(input())

for _ in range(t):
    m, n, c = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(c):
        x, y = map(int, input().split())
        graph[y][x] = 1

    cnt = 0

    for i in range(n):  # 행
        for j in range(m):  # 열
            if graph[i][j]:
                bfs(i, j)
                cnt += 1
    print(cnt)
