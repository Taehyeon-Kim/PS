import sys
sys.setrecursionlimit(10**6)

result = []
diff = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [1, -1], [-1, 1], [-1, -1]]

while True:
    # 입력부
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    visited = [[False] * w for _ in range(h)]  # 방문 확인할 배열
    arr = []       # 섬과 바다 지도 담을 배열
    ground = []    # 땅만 담을 배열
    count = 0      # 섬의 개수 저장할 변수

    # 땅만 뽑아내기 위해서 배열 컨트롤
    for i in range(h):
        arr.append(list(map(int, input().split())))
        for j in range(w):
            if arr[i][j] == 1:
                ground.append([i, j])

    def dfs(x, y):
        # 아직 방문하지 않았다면
        if not visited[x][y]:
            # 방문처리
            visited[x][y] = True
            for d in diff:
                # 8개의 방향에 대해서 확인
                new_x, new_y = x + d[0], y + d[1]
                # 영역 안에 있고, 땅이라면 dfs 재귀 호출
                if 0 <= new_x < h and 0 <= new_y < w and arr[new_x][new_y] == 1:
                    dfs(new_x, new_y)

    for g in ground:  # g는 처음 입력 받은 땅의 좌표입니다. [x, y]
        if not visited[g[0]][g[1]]:
            count += 1
            dfs(g[0], g[1])

    print(count)
