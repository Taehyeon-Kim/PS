'''
- 규칙을 잘 찾아야 하는데
- 생각을 해보면 각 단계로 내려갈수록 최대의 합이 되도록 선택해 더해주면 되는 문제이다.
- 이전에 값을 기억하고 있다가 계속해서 최대의 합이 되도록 선택해 더해주면 되는 문제이다.
- 주의할 점은 그리디처럼 순간순간 최댓값을 고르는게 아니라 최대의 합이 되도록 더해줘야한다.
'''


def solution(triangle):
    l = len(triangle)
    dp = [[0] * i for i in range(1, l + 1)]  # dp 테이블
    dp[0][0] = triangle[0][0]

    for i in range(1, l):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][j] += triangle[i][j] + dp[i-1][j]
            elif j == len(triangle[i]) - 1:
                dp[i][j] += triangle[i][j] + dp[i-1][j-1]
            else:
                dp[i][j] += triangle[i][j] + max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[l-1])
