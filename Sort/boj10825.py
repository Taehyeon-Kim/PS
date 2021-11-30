import sys
input = sys.stdin.readline

students = []

n = int(input())
for _ in range(n):
    name, kor, eng, math = input().split()
    students.append((name, int(kor), int(eng), int(math)))

answer = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))

for student in answer:
    print(student[0])
