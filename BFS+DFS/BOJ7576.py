'''
익은 토마토 : 1
익지 않은 토마토 : 0
빈칸 : -1

시작점이 여러개

이전에 풀었을 때는 못 풀었던 것 같은데 지금 보니까 기본적인 유형이었다.
유형 중에서도 시작점이 여러개인 BFS 문제이다.

이번에는 중요한 포인트를 하나 얻었는데
행, 열에 대한 정확한 입력을 받아야한다는 것이다. 너무나 당연하게 왼쪽으로 들어오는 값이 행이라고 생각했는데 열이었다. 그래서 런타임, 컴파일 에러 둘 다 만남..ㅎ 주의하자 
'''
from collections import deque

m, n = map(int, input().split())
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

dist = [[0 for _ in range(m)] for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            q.append((i, j))
        if board[i][j] == 0:
            dist[i][j] = -1

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

answer = 0
for i in range(n):
    for j in range(m):
        if dist[i][j] == -1:
            print(-1)
            exit(0)
        answer = max(answer, dist[i][j])
print(answer)
