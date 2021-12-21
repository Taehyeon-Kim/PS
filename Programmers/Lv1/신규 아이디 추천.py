# - 날짜 : 21.12.21
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 2021 카카오 블라인드 공채
# - 문자열, 구현

# Check List
# [] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제
# - [x]  함수 찾아봐서 푼 문제

# 정규식으로 풀면 어떨까라는 생각이 처음에 들었다.
# 그냥 찐구현 + 문자열 조작 문제


def filtering(string: str):
    char = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    for s in string:
        if s not in char:
            string = string.replace(s, "")
    return string


def replacePoint(string: str):
    result = ""
    for s in string:
        if s == "." and result and result[-1] == ".":
            continue
        result += s
    return result


def solution(new_id):
    answer = new_id

    answer = answer.lower()
    answer = filtering(answer)
    answer = replacePoint(answer)
    answer = answer.strip(".")

    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15].strip(".")
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1]

    return answer
