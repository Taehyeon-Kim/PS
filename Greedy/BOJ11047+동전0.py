# 입력 및 변수
n, k = map(int, input().split())         # 동전 종류 개수, K원
coins = [int(input()) for _ in range(n)] # 동전을 종류대로 담는다.(오름차순)
count = 0

# 정렬
coins.sort(reverse=True)                # 내림차순으로 정렬

# 계산
for coin in coins: # 큰 동전부터 반복해서 체크할거야
    # if 조건: 조건은 어떻게 되어야 할까요? (조건이 필요없겠다.)
        count += k//coin # 몫만큼 더해준다. (동전 개수)
        k %= coin
# 출력
print(count)
