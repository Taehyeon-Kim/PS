# - 날짜 : 21.12.23
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 위클리 체인지
# - 3m

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제

# 조건 잘 보기 : 금액이 부족하지 않으면 0을 return


def solution(price, money, count):
    prices = [price * i for i in range(1, count+1)]
    diff = sum(prices) - money
    return diff if diff >= 0 else 0
