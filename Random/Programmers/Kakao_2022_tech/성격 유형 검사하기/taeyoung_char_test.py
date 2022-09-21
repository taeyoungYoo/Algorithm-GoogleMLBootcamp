'''
    2022 Kakao tech intership
    성격 유형 검사
    - 문자열 매칭 문제
'''

import collections


def solution(survey, choices):
    answer = ''
    score = collections.defaultdict(int)
    # 점수와 인덱스 일치
    cvt_score = [0, 3, 2, 1, 0, 1, 2, 3]
    # 타입별 최종 점수 계산
    for s, c in zip(survey, choices):
        if c > 4:
            score[s[1]] += cvt_score[c]
        else:
            score[s[0]] += cvt_score[c]
    # 지표별 최종 성격 도출
    if score["T"] > score["R"]:
        answer += "T"
    else:
        answer += "R"
    if score["F"] > score["C"]:
        answer += "F"
    else:
        answer += "C"
    if score["M"] > score["J"]:
        answer += "M"
    else:
        answer += "J"
    if score["N"] > score["A"]:
        answer += "N"
    else:
        answer += "A"

    return answer