'''
n m : 1 ~ n 까지 중복 없이 M개를 고른 수열
3 1 : 1 ~ 3 까지 중복 없이 1개를 고른 수열 / 1 2 3
4 2 : 1 ~ 4 까지 중복 없이 2개를 고른 수열 / 

백트래킹 + 재귀
'''

n, m = map(int, input().split())  # 열, 행
arr = [0] * (m+1)
isUsed = [0] * (n+1)


def backT(k: int):
    if k == m:
        for i in range(m):
            print(arr[i], end=" ")
        return

    for i in range(1, n+1):
        if isUsed[i] == 0:
            arr[k] = i
            isUsed[i] = 1
            backT(k+1)
            isUsed[i] = 0


backT(0)
