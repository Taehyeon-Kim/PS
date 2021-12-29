# - 날짜 : 21.12.29
# - 작성자 : 김태현
# - 프로그래머스 Lv2
# - 2017 팁스타운
# - 스택 기본

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제
# - [x]  예상 시간보다 오래 걸린 문제

'''
10:54-11:19
- (반복) 두개씩 짝짓고, 제거
- 리스트 2개
    - 리스트 1 (원본 데이터) : 데이터 pop
    - 리스트 2 (스택) : 데이터 비교 후 짝이 맞으면 데이터 pop
- 리스트 2가 비어있으면 1
'''

# [baabaa] [] b
# [aabaa] [b] a,b
# [abaa] [ba] a,a - del
# [baa] [b] b,b - del
# [aa] []
# [a] [a]
# [] []


def solution(s):
    answer = -1

    strings = list(s)  # 리스트로 사용하기 위함
    stack = []

    for s in strings:
        if stack == []:
            stack.append(s)
        else:
            if stack[-1] == s:
                stack.pop()
            elif stack[-1] != s:
                stack.append(s)

    return 1 if len(stack) == 0 else 0
