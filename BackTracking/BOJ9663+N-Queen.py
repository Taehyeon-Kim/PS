'''
BOJ 9663 N-Queen
Backtracking + DFS
134084 KB / 5004ms
'''

n = int(input())  # n = 1 ~ 14

cnt = 0
isused1 = [0] * 40
isused2 = [0] * 40
isused3 = [0] * 40


def backT(x: int):
    if x == n:
        global cnt
        cnt += 1
        return  # 마지막 행까지 말을 놓았을 때 리턴
    for y in range(n):
        if isused1[y] or isused2[x+y] or isused3[x-y+n-1]:
            continue
        isused1[y] = 1
        isused2[x+y] = 1
        isused3[x-y+n-1] = 1
        backT(x+1)
        isused1[y] = 0
        isused2[x+y] = 0
        isused3[x-y+n-1] = 0


backT(0)
print(cnt)
