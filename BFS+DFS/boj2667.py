# - 날짜 : 21.01.03
# - 작성자 : 김태현
# - BOJ 2667 단지번호붙이기
# - BFS

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제

from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    size = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny]:
                graph[nx][ny] = 0
                q.append((nx, ny))
                size += 1
    return size


if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    count = 0
    size = []

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                count += 1
                size.append(bfs(i, j))

    size.sort()

    print(count)
    for i in size:
        print(i)
