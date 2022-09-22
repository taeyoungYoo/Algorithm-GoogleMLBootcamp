'''
성격유형 검사지
1번 RT 
2번 CF
3번 JM
4번 AN

동점일때는 RCJA (알파벳이 빠른 순)

딕셔너리 만들고

choices의 값이 4보다 작으면 앞의 항목에 4를 뺀 절대값을 넣어준다.
항목별로 비교후 answer에 값을 넣어준다.
'''
def solution(survey, choices):
    # 점수를 담을 딕셔너리 만들기
    score_table = {'R':0, 'T':0,
                   'C':0, 'F':0,
                   'J':0, 'M':0,
                   'A':0, 'N':0}

    # 검사항목과 평가 진행
    for s, c in zip(survey, choices):
        s_list = list(s)
        # 4보다 작은경우 앞의 항목에 점수를 더한다.
        # 더할 점수는 4를 뺀 절대값과 같다
        if c < 4:
            score_table[s_list[0]] += abs(c-4)
        else:
            score_table[s_list[1]] += abs(c-4)
    
    # 순서대로 검사항목을 순환하며
    answer = ''
    test_list = [['R','T'],['C','F'],['J','M'],['A','N']]
    for i,j in test_list:
        # 뒤의 항목이 값이 클 경우 뒷 쪽의 성격 유형이 answer에 더해지고
        if score_table[i] < score_table[j]:
            answer+=j
        # 그외의 경우 앞의 성격 유형이 answer에 더해진다.
        else:
            answer+=i
    
    return answer
