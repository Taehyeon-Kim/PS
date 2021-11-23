import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

left = 0
right = max(trees)

while left <= right:
    tree_heights = 0
    mid = (left + right) // 2
    for tree in trees:
        if tree > mid:
            tree_heights += tree - mid

    if tree_heights >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)
