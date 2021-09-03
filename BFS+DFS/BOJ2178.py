'''
BFS 응용(1) - 거리 측정
거리 측정 중 최단 경로 문제(각 인접 거리가 1일 때)
- dist 배열을 만든다.
  - 해당 배열로 거리와 방문 여부를 판단한다.
- 나머지 로직은 같음

>> 입력을 항상 주의해서 받자 - 입력을 이상하게 받아서 런타임, 컴파일 에러가 계속 남
'''

from collections import deque

# 입력
n, m = map(int, input().split())
board = [input() for _ in range(n)]
dist = [[-1 for _ in range(m)] for _ in range(n)]

# 상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 덱 생성
q = deque()
dist[0][0] = 0
q.append((0, 0))

# BFS
while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # 범위 안에 있는지 체크, 방문 여부 체크, 갈 수 있는 길인지 체크
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '1':
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

# 문제 특성 상 처음과 끝도 거리에 포함되어서 +1
print(dist[n-1][m-1] + 1)
