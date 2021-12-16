# - 날짜 : 21.12.15
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 2021 Dev-Matching: 웹 백엔드 개발자(상반기)
# - 해시, 완전탐색
# - 15-20m

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제


'''
0이 들어있다면 0이 모두 정답인 경우 - 최고 점수
0이 들어있다면 0이 모두 오답인 경우 - 최저 점수

순위 
- 당첨내용 : 해시(딕셔너리)로 접근
전략 
- 완전탐색(로또의 길이가 한정되어 있음)
- 일단 0을 제외한 숫자가 win_nums 안에 있는지 체크 + count
- 0의 개수를 더한 것이 최고 점수
- 아무것도 안 한 것이 최저 점수
'''


# 개선 코드

def solution(lottos, win_nums):
    # count : rank
    ranks = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5
        # 없으면 6등으로 계산
    }

    def getRank(count, ranks):
        rank = 6
        if count in ranks:
            return ranks[count]
        return rank

    # 로또 개수가 몇 개나 일치하는지 계산 로직
    zeroCount = 0
    count = 0

    for lotto in lottos:
        if lotto == 0:
            zeroCount += 1
        if lotto in win_nums:
            count += 1

    # 등수 개산하는 로직
    high = getRank(count + zeroCount, ranks)
    low = getRank(count, ranks)

    return [high, low]


assert solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]) == [3, 5]
assert solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]) == [1, 6]
assert solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]) == [1, 1]
