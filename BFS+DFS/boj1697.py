from collections import deque


def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for i in (x-1, x+1, x*2):
            if 0 <= i <= 100000 and not dist[i]:
                dist[i] = dist[x] + 1
                q.append(i)


n, k = map(int, input().split())
dist = [0] * 100001
bfs()
