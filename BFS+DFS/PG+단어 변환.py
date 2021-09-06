'''
- 단어 비교해주는 함수 작성 (각 단어를 비교했을 때, 알파벳 1개만 차이나는지)
- BFS로 탐색 진행
- 큐에 담는 방식, (단어, 변환 횟수(depth))
'''

from collections import deque


def compareWords(begin, word):
    count = 0
    for i in range(len(begin)):
        if begin[i] == word[i]:
            continue
        count += 1

    return True if count == 1 else False


def solution(begin, target, words):
    answer = 0
    wordLength = len(words)
    visited = [0] * wordLength
    count = 0

    q = deque([(begin, count)])
    while q:
        v, c = q.popleft()
        for i in range(wordLength):
            if not visited[i] and compareWords(v, words[i]):
                q.append((words[i], c + 1))
                visited[i] = 1
                if words[i] == target:
                    return c + 1

    print(0)

    return answer
