#  최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음으로 구성되어 있다고 알려져 있다
#  알파벳이 암호에서 증가하는 순서로 배열

from itertools import combinations

# 입력
'''
4 6
a t c i s w
'''
l, c = map(int, input().split())  # 4 6
alphas = list(input().split())   # ['a', 't', ... 'w']
alphas = sorted(alphas)

results = []

# 과정
for i in combinations(alphas, l):
    m_flag = False  # 모음이 들어가있는지를 판단할 변수
    j_flag = 0     # 자음이 몇 개 들어가있는지 판단할 변수
    word = ''.join(i)  # acis

    # 체킹
    for i in word:  # acis -> a c i s
        if i in "aeiou":  # 알파벳이 모음인지?
            m_flag = True
        else:  # 자음
            j_flag += 1

    if m_flag == True and j_flag >= 2:  # 조건 만족하나요?
        print(word)
