n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]
ans = []
cur = 0    # 시작커서

while len(nums) > 0:
    cur = (cur + (k-1)) % len(nums)  # ✨
    elem = nums.pop(cur)
    ans.append(elem)

print("<", end="")
for i in range(n-1):
    print(str(ans[i]), end=", ")
print("%d>" % (ans[n-1]))
