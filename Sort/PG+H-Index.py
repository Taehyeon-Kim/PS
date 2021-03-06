'''
손으로 우선 생각함

1. 정렬 (내림차순으로 해보자) -> 최댓값을 리턴해야하니까
2. 각 원소를 기준으로 잡는다. => H로 잡는다는 뜻
3. 조건을 둔다.
    H 보다 크거나 같 count
    H 보다 작거나 같 count
4. H, B, S 비교해서 세 개가 같으면 바로 return

'''


# 틀린 풀이 (테스트 케이스만 정답)
# def solution(citations):
#     citations.sort(reverse=True)
#     for h in citations:
#         B = 0
#         for citation in citations:
#             if h <= citation:
#                 B += 1
#         if B >= h:
#             return h

# 정답 풀이 참고
# 아이디어를 떠올리는 게 중요했던 문제
def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)
