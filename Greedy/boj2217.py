'''
boj 2217 로프
완전탐색이 필요없이 내림차순 정렬을 해서 필요한 경우만 탐색한다.

1. 최대가 되려면 큰 값부터 뽑아서 조합을 만들어
2. 1 ~ K개씩 뽑는 조합이 있는데
	- 1개를 뽑는 경우를 생각해보면, K번 모든 조합을 보는 게 아니라 가장 큰 값이 나올 수 있는 경우만 생각하는 방식으로 접근(그리디하게)
'''

k = int(input())
ropes = [int(input()) for _ in range(k)]

ropes.sort(reverse=True)  # 내림차순 정렬

# 이 아이디어가 중요
for i in range(k):
    ropes[i] *= (i+1)  # w * k = 최대 중량 * 로프 개수

print(max(ropes))
