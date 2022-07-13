# 시은 풀이 - 4636ms
def solution(str1, str2):
    n = len(str1)
    max_len = 0

    for i in range(n):
        # 불가능한 경우
        if str1[i] not in str2:
            continue

        # 부분 문자열
        sub_str = str1[i:i+max_len]

        # 불가능한 경우
        if sub_str not in str2:
            continue

        for j in range(i + max_len, n):
            sub_str += str1[j]
            if sub_str in str2:
                max_len = j - i + 1
            else:
                break

    return max_len


str1 = input()
str2 = input()

print(solution(str1, str2))