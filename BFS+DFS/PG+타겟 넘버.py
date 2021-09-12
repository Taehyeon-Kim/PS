'''
부호는 +, - 중 하나
트리로 그려볼 수 있겠다는 것은 떠올림
그렇다면 트리를 순회할 수 있는 BFS, DFS 중에 하나로 풀 수 있지 않을까?

아이디어는 떠올렸으나, 구현은 못함
'''


def solution(numbers, target):
    tree = [0]
    for i in numbers:
        sub_tree = []
        for j in tree:
            sub_tree.append(j + i)
            sub_tree.append(j - i)
        tree = sub_tree
    return tree.count(target)
