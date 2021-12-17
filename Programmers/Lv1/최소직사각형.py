# - 날짜 : 21.12.15
# - 작성자 : 김태현
# - 프로그래머스 Lv1
# - 위클리 챌린지
# - 구현

# Check List
# [x] 스스로 해결한 문제
# []  스스로 해결하지 못한 문제
# - []  아이디어를 떠올리지 못한 문제
# - []  아이디어를 떠올렸으나 구현을 하지 못한 문제
# - []  시간이 너무 오래 걸린 문제 (1시간 30분 이상)
# - []  다른 블로그의 풀이를 참고해서 푼 문제
# - [x]  예상 시간보다 오래 걸린 문제

'''
- 주어진 size 배열을 가져다가 사용하는데, 원소의 순서만 재배치해서 사용
- 큰 사이즈를 왼쪽으로, 작은 사이즈를 오른쪽으로 모두 몰면 되지 않을까?
- 왜냐하면 가장 큰 사이즈 중 큰 사이즈와 작은 사이즈 중 큰 사이즈는 서로 반대편에 있어야 하니까
- 아이디어) 그럼 그냥 원소를 쭉 나열한 다음 반으로 가르고 각각 그룹에서 가장 큰 사이즈를 곱하기만 하면 됨
'''

# 너무 쉽게 돌아가려다 틀린 풀이
# def solution(sizes):
#     sizeArr = []
#     sizeArrLength = len(sizes) * 2

#     # 1차원 배열의 형태로 변환 위함
#     for size in sizes:
#         # size = [60, 50]
#         sizeArr += size

#     # 정렬
#     sizeArr = sorted(sizeArr)

#     # 계산 로직
#     w = max(sizeArr[0:sizeArrLength//2])
#     h = max(sizeArr[sizeArrLength//2:])

#     return w*h

# 정답 풀이


def solution(sizes):
    wmax, hmax = 0, 0

    for w, h in sizes:
        size = [w, h] if w > h else [h, w]
        wmax = max(wmax, size[0])
        hmax = max(hmax, size[1])

    return wmax * hmax
