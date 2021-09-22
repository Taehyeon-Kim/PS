n, s = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0


def backT(cur: int, total: int):
    global cnt
    if cur == n:
        if total == s:
            cnt += 1
            return
    else:
        backT(cur+1, total)
        backT(cur+1, total + nums[cur])


# 실행
backT(0, 0)

if s == 0:
    cnt -= 1
print(cnt)
