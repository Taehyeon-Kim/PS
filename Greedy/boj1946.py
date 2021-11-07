'''
boj 1946 신입사원 그리디

반복문을 돌면서 매순간 2명을 비교하는 것이 아니라
기준값을 계속해서 갱신을 해주어야 한다.

나보다 서류, 면접 점수가 모두 높은 사람이 있어서는 안된다!! (말장난..)
'''

import sys
input = sys.stdin.readline  # 입력에 들어가는 시간을 최대한 줄이기 위함

t = int(input())       # 테스트케이스 수

for _ in range(t):     # 테스트케이스 속에서 계산 시작
    n = int(input())   # 지원자 숫자
    grades = []
    for _ in range(n):  # 성적 입력받기
        grades.append(tuple(map(int, input().split())))
    grades.sort()  # 1차 기준으로 오름차순 정렬 (순위로 따져야 함)

    count = 0
    value = grades[0][1]

    for i in range(1, n):  # 인덱스 에러 주의
        if value > grades[i][1]:
            # 그래야 통과
            value = grades[i][1]
            count += 1

    print(count+1)
