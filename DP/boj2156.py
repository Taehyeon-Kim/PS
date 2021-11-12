'''
boj 2156 포도주 시식
아이디어를 떠올리기 좀 복잡한 문제
하나씩 나열해보는 것이 가장 좋은 방법인 것 같다.
'''
# 입력
n = int(input())
wines = [0] + [int(input()) for _ in range(n)]

# DP 테이블
dp = [0] * (n+2)

for i in range(1, n+1):
    # 초기값 세팅을 조건으로 대신 해줌.
    if i == 1:
        dp[1] = wines[1]
    elif i == 2:
        dp[2] = wines[1] + wines[2]
    # 점화식
    else:
        dp[i] = max(dp[i-1], wines[i]+dp[i-2], wines[i]+wines[i-1]+dp[i-3])

print(dp[n])
