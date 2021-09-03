'''
BOJ 1926 그림
- BFS에서 살짝 응용된 형태이나 가장 기본적인 유형 중 하나
- 상하좌우 컨트롤 (dx, dy 이용)
- 시작점이 여러 개가 되는 경우 배열을 돌면서 각각의 경우를 체크
  - 이 때, 이미 방문한 지점이나 갈 수 없는 곳은 skip 하면서 체크해야 함
'''

from collections import deque  # deque import

# input
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

count = 0             # 그림 개수
maxSize = 0           # 그림 면적
dx = [1, -1, 0, 0]    # dx 방향
dy = [0, 0, 1, -1]    # dy 방향

# 얘 같은 경우 모든 길이 연결된 것이 아니기 때문에
# bfs를 여러번 돌리게 되는 문제
# 따라서 함수로 관리하는 게 더 좋아보인다.


def bfs(x, y):
    q = deque()             # 덱 생성
    graph[x][y] = 0         # 항상 방문지점은 미리 체크를 하자
    q.append((x, y))        # 그런 다음에 큐에 넣기
    size = 1

    while q:                # 큐가 빌 때까지 반복
        x, y = q.popleft()  # 보통 다차원 배열이 배경이 되기 때문에 x, y 좌표가 필요
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위와 방문유무 체크하기 💥
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]:
                graph[nx][ny] = 0     # 방문 표시를 꼭 놓치면 안 됨
                q.append((nx, ny))
                size += 1
    return size


# bfs를 여러 개 돌리는 유형
# 시작지점이 여러개
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            maxSize = max(maxSize, bfs(i, j))
            count += 1

print(count)
print(maxSize)
