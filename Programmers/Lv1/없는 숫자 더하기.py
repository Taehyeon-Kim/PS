# - 날짜 : 21.12.26
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 월간 코드 챌린지
# - 구현

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제


def solution(numbers):
    answer = 0
    for number in numbers:
        if number in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
            answer += number
    return 45 - answer
