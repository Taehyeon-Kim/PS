'''
- 0으로 bridge의 개수를 맞춰주는 아이디어.
- 코드는 간단한데 생각보다 어려웠다.
'''


def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length

    while q:
        q.pop(0)
        time += 1

        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)

    return time
