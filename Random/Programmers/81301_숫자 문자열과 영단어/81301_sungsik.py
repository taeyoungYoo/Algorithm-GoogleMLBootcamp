def solution(s):
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
                'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    answer = ''
    tmp = ''

    for i in s:
        if 123 > ord(i) > 96:       # i가 알파벳이면 tmp에 붙이기
            tmp += i
            if tmp in num_dict:     # 붙인 tmp 문자열이 딕셔너리에 있으면 answer에 붙이기
                answer += str(num_dict[tmp])
                tmp = ''
        elif 58 > ord(i) > 47:      # i가 숫자면 answer에 붙이기
            answer += i

    return int(answer)              # answer를 정수형으로 반환


s = "23four5six7"
print(solution(s))


