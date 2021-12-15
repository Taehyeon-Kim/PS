# - 날짜 : 21.12.15
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 2021 카카오 채용연계형 인턴십
# - 해시, 문자열, 완전탐색

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제


def solution(s):
    words = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    for key in words.keys():
        if key in s:
            s = s.replace(key, words[key])

    return int(s)
