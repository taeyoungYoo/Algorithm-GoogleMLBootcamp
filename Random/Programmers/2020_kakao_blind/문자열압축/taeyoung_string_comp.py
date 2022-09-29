'''
    kakao 2020 blind
    문자열 압축
    - 압축된 문자열 길이가 최소가되는 압축 단위 구하기
    - 완전탐색
'''
def compression(s, n):
    # 탐색 범위는 마디의 몫
    lim = len(s) // n
    ret = ""
    for i in range(0, lim):
        # 검사 부분 문자열 및 남은 문자열 업데이트
        unit = s[:n]
        s = s[n:]
        count = 1
        # 남은 부분의 길이를 고려한 탐색 범위 업데이트
        new_lim = len(s) // len(unit)
        for j in range(0, new_lim):
            if s[:n] == unit:
                count += 1
                s = s[n:]
            else:
                break
        # 압축 가능하면 숫자 더하고 할 수 없다면 그냥 붙이기
        if count != 1:
            ret += str(count)+unit
        else:
            ret += unit
        # 문자열이 다 압축되었다면 break
        if len(s) == 0:
            break
    return ret + s


def solution(s):
    answer = 1001
    # edge case. s가 한자리
    if len(s) == 1:
        return 1
    # 절반 이하의 길이를 마디로 설정해 검사
    lim = len(s) // 2
    for i in range(1, lim+1):
        ret = len(compression(s, i))
        if answer > ret:
            answer = ret
    return