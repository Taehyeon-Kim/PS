'''
key:value 형태로 자료 관리 하면 될 듯
value는 int형으로 관리해서, enter면 +1 leave면 -1
마지막에는 내림차순 정렬
'''

# input
n = int(input())
table = dict()

# logic
for _ in range(n):
    name, inOut = input().split()
    if inOut == "enter":
        table[name] = 1
    else:
        # 메모리 최소화 및 속도향상을 위해 leave(퇴근)인 경우 del로 메모리 해제 💥
        del table[name]

# sort
table = sorted(table.items(), reverse=True)

# output
for key, val in table:
    print(key)

'''
# 시간초과 풀이
# input
n = int(input())
table = dict()

# logic
for _ in range(n):
    name, inOut = input().split()
    value = 1 if inOut == "enter" else -1
    table[name] = table.get(name, 0) + value

# sort
table = sorted(table.items(), reverse=True)

# output
for key, val in table:
    if val == 0: continue
    print(key)
'''
