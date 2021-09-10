'''
1. {시작점 - [도착점들]} 쌍의 그래프를 만든다.
2. 도착점들의 리스트는 역순으로 정렬시킨다.
3. DFS 알고리즘을 통해 모든 점을 순환시킨다. (완전탐색의 느낌)
'''


def solution(tickets):
    routes = dict()

    for (start, end) in tickets:
        routes[start] = routes.get(start, []) + [end]

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]  # top

        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]

    path.reverse()
    return path
