'''
boj 1026 보물 그리디

b가 정렬되면 안 된다는 조건이 있지만, 정렬해서도 풀리는 문제
아이디어는 S가 최대가 되기 위해서는
한쪽 배열의 최대값과 한쪽 배열의 최소값이 곱해져야 한다는 것이다.
(재배열 부등식이라는 증명이 필요하다는 것이다.)
'''

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()  # a만 정렬하는 것으로 수정

s = 0
for i in range(n):
    x = a[i]  # a의 최솟값
    y = b.pop(b.index(max(b)))  # b의 최댓값을 pop
    s += x * y
print(s)
