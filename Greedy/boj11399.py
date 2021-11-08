'''
boj 11399 ATM 그리디
돈 뽑는데 적게 걸리는 사람부터 뽑으면 되는 문제 (정렬 필요)
'''

answer = 0
n = int(input())
times = list(map(int, input().split()))
times.sort()

wait = 0
for i in range(n):
    wait += times[i]
    answer += wait
print(answer)
