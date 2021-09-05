'''
BFS 응용(2) - 시작점의 종류가 2가지 일때

런타임에러가 발생하는 이유 중 하나는 실행 중에 배열의 인덱스를 넘어가는 경우인데
그렇기 때문에 배열의 크기를 잘 설정해주어야 한다.

이 문제에서 너무 많이 틀려서 스트레스를 받고 있었는데 오류의 원인이
dist1 = [[-1 for _ in range(c)] for _ in range(r)]
dist2 = [[-1 for _ in range(c)] for _ in range(r)]

이렇게 배열을 잘못 설정해주었기 때문이다.
dist1 = [[-1 for _ in range(r)] for _ in range(c)]
dist2 = [[-1 for _ in range(r)] for _ in range(c)]
'''

from collections import deque

# 행, 열
r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
dist1 = [[-1 for _ in range(c)] for _ in range(r)]
dist2 = [[-1 for _ in range(c)] for _ in range(r)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q1 = deque()  # 불
q2 = deque()  # 지훈

for i in range(r):
    for j in range(c):
        if board[i][j] == 'F':
            q1.append((i, j))
            dist1[i][j] = 0
        if board[i][j] == 'J':
            q2.append((i, j))
            dist2[i][j] = 0

while q1:
    x, y = q1.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= r or ny < 0 or ny >= c):
            continue
        # 이미 방문했거나 벽이라면
        if (dist1[nx][ny] >= 0 or board[nx][ny] == '#'):
            continue
        dist1[nx][ny] = dist1[x][y] + 1
        q1.append((nx, ny))

while q2:
    x, y = q2.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx < 0 or nx >= r or ny < 0 or ny >= c):
            print(dist2[x][y] + 1)
            exit(0)
        if (nx < 0 or nx >= r or ny < 0 or ny >= c):
            continue
        if dist2[nx][ny] >= 0 or board[nx][ny] == '#':
            continue
        if dist1[nx][ny] != -1 and dist1[nx][ny] <= dist2[x][y] + 1:
            continue
        dist2[nx][ny] = dist2[x][y] + 1
        q2.append((nx, ny))

print("IMPOSSIBLE")
