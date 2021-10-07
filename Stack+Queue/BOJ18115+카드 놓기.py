'''
파이썬에서 강력한 자료구조 중 하나인 덱을 사용하는 문제
덱을 사용할 경우 리스트의 앞뒤로 원소를 추가하거나 제거할 수 있어서 매우 효율적이다.
'''

from collections import deque

n = int(input())                         # 카드 개수
skills = deque(input().split())          # 기술
cards = deque(range(1, n+1))             # 카드 1 ~ N
result = deque([])                       # 결과 덱


while skills:
    skill = skills.pop()
    card = cards.popleft()
    if skill == "1":
        result.appendleft(card)
    elif skill == "2":
        result.insert(1, card)
    elif skill == "3":
        result.append(card)
print(*result)                           # 덱을 출력하고 싶으면 *(asterisk) 사용
