'''
boj 2748 피보나치 수 2
- bottom-up으로 접근
- DP의 가장 기초적인 예제
'''

n = int(input())
dp = [0] * 91  # 90으로 만들어놨다가 런타임 에러 발생

dp[0] = 0
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
