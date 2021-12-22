# - 날짜 : 21.12.22
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 월간 코드 챌린지 시즌 1
# - 구현(조합, 중복 제거, 정렬)
# - 15-20m

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제

# 1) 반복문을 이용한 풀이
# def solution(numbers):
#     answer = []

#     for i in range(0, len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])

#     return sorted(list(set(answer)))

from itertools import combinations

# 2) combinations(조합)을 이용한 짧은 풀이
# combinations도 꽤나 사용된다. 기억해두자.


def solution(numbers):
    answer = [nums[0] + nums[1] for nums in combinations(numbers, 2)]
    return sorted(list(set(answer)))
