# (키, 몸무게) 리스트 입력받기
n = int(input())
sizes = [list(map(int, input().split())) for _ in range(n)]

# 등수 비교
for i in range(n):
    count = 0
    for j in range(n):
        if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]:
            count += 1
    print(count+1, end=" ")
