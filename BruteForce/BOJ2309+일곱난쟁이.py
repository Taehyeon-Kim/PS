'''
입력 값 - 9명의 난쟁이 키
출력 - 합이 100이 되는 7명의 난쟁이 키를 오름차순으로 출력

- 9명 중 7명의 조합을 뽑기 (itertools, for)
- 7명의 키의 합이 100이 되어야 함
- 출력 시 오름차순으로 출력
'''

from itertools import combinations

heights = [int(input()) for i in range(9)]  # 키 입력 (배열)

for combs in list(combinations(heights, 7)):
    # print(combs)
    if sum(combs) == 100:
        # print(sorted(combs))
        for height in sorted(combs):
            print(height)
        break  # print가 또 될 수 있음
