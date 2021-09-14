'''
- DP 문제
- 행렬의 행과 열에 대한 파악은 항상 중요한 문제이다.
- 1_000_000_007로 나눠주는 것이 매순간 이루어져야하는 것도 체크해야할 부분이었다.
- 행과 열을 1씩 증가시켜주는 것도 좋은 스킬인 것 같다.
'''


def solution(m, n, puddles):
    puddles = [[j, i] for [i, j] in puddles]
    dp = [[0] * (m + 1) for _ in range(n + 1)]  # dp 테이블

    dp[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 시작 위치 제외
            if i == 1 and j == 1:
                continue

            # 웅덩이
            if [i, j] in puddles:
                dp[i][j] = 0

            # 좌측, 위 계산
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1_000_000_007

    return dp[n][m]
