'''
phone_book : 전화번호 배열
어떤 번호(원소)가 다른 번호의 접두어인 경우가 있으면 T/F

이 문제도 원소의 각자리를 비교하거나 해야 하는데 정렬이 필요할 것 같고 (짧 -> 긴 순서로)
완전탐색으로 풀면 시간초과 나는 것 같아서 다른 방법 고민(생각안나면 완전탐색으로라도 접근)

아이디어...
1) 짧은것 단위로 끊어서 생각해봐도 좋을 것 같기도 하고
119 976 119

2) 정렬이 길이순이아니고 크기순이라면? 그럼 한 칸씩만 이동하면서 앞뒤로만 체크해도 될 것 같은데.
119 120 136 976
'''


def solution(phone_book: list):
    phone_book.sort()

    # 반복문은 한 번만 돌면 됨
    for i in range(len(phone_book) - 1):
        # print(phone_book[i], phone_book[i+1][0: len(phone_book[i])])
        if phone_book[i] == phone_book[i+1][0: len(phone_book[i])]:
            return False

    return True


if __name__ == '__main__':
    assert solution(["119", "97674223", "1195524421"]) == False
    assert solution(["123", "456", "789"]) == True
    assert solution(["12", "123", "1235", "567", "88"]) == False
