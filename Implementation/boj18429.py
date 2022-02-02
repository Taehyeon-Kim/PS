from itertools import permutations

n, k = map(int, input().split())
kits = list(map(int, input().split()))
count = 0

for kit in permutations(kits):
    weight = 500
    for i in range(n):
        weight += kit[i] - k
        if weight < 500:
            break
    else:
        count += 1

print(count)
