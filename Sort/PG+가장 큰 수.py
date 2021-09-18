# 각 숫자의 자리를 비교해서 더 큰 수가 앞으로 오도록 하면 된다.
# sort함수에다가 적절하게 lambda를 이용하면 될 것 같다.
# 자릿수를 비교하려면 문자열 형태가 더 편할 듯?
# 마지막에 str int는 '0000' 같은 걸 '0'으로 바꾸기 위해서 해야함 => 아니면 11번 테케가 틀림


def solution(numbers):
    answer = list(map(str, numbers))
    answer.sort(key=lambda x: x*3, reverse=True)
    return "".join(answer)


# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))
