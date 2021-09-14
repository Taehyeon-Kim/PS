'''
이 문제는 뭔가 수식만 잘 세우면 될 것 같다.
규칙을 잘 찾으라는 뜻
손으로 그려보라는 뜻

(2+1)(1+1)-1 = 3*2-1 = 5
(3+1)-1 = 3
(종류+1)(종류+1) - 1

#1
headgear : 2
eyewear : 1

1종류 조합 3
2종류 조합 2

#2
face : 3

1종류 조합 3

#3
face : 2
top : 1
bottom : 1
outer : 1

1종류 5
2종류 2+2+2+1+1+1
3종류 2+2+2+1
4종류 2
'''

def solution(clothes):
    # 딕셔너리 생성
    dict = {}
    for cloth in clothes:
        if cloth[1] in dict.keys():
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    
    answer = 1
    for val in dict.values():
        answer *= (val + 1)
    
    return answer - 1
    
assert solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]) == 5
assert solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]) == 3