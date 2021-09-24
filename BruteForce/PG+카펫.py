'''
brown : 가장 자리 , yellow : 중앙
1) 10 2
1 1 1 1
1 0 0 1
1 1 1 1

yw + 2 = bw
yh + 2 = bh
bw * bh = brown + yellow

- 규칙을 파악해서 접근
- 약수 성질을 이용해서 접근
- 약수는 어차피 세트가 (1 12), (12 1) 이런식으로 반복되니까 중복되는 것은 체크 생략하기
'''


def solution(brown, yellow):
    answer = []

    totalTiles = brown + yellow  # 전체 타일 수

    for i in range(1, totalTiles // 2):
        if totalTiles % i == 0:
            x, y = i, totalTiles//i
            if x - 2 > 0 and y - 2 > 0:
                if ((x-2) * (y-2)) == yellow:
                    answer = [x, y]

    return answer


assert solution(10, 2) == [4, 3]
assert solution(8, 1) == [3, 3]
assert solution(24, 24) == [8, 6]
