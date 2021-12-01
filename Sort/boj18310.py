import sys
input = sys.stdin.readline

n = int(input())
houses = list(map(int, input().split()))

houses.sort()
print(houses[(n-1)//2])  # -1을 해주는 이유는 짝수인경우 중간값이 2개기 때문에 더 작은거 선택

# 중간값이 2개일때 둘중에 어느 하나를 선택해도 같은 이유는,
# 둘의 차이가 전체적으로 +/- 되기 때문에 총합은 일정
