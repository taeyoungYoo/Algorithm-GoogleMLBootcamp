import math
def solution(n, k):
    def convert(n, k):
        ret = ""
        q, r = divmod(n, k)
        ret = str(r) + ret
        while q != 0:
            q, r = divmod(q, k)
            ret = str(r) + ret
        return ret

    # 소수 판별 함수
    def check_prime(cand):
        if cand == 1:
            return False
        lim = math.floor(math.sqrt(cand))
        for i in range(2, lim+1):
            if cand % i == 0:
                return False
        return True

    # Main
    # 받아서 진법 변환
    converted_num = list(convert(n, k))
    # 변환된 string을 stack에 넣으며 처리
    check_stack = []
    answer = 0

    while converted_num:
        val = converted_num.pop()
        if val == '0' and len(check_stack) > 0:
            if check_prime(int("".join(check_stack))):
                answer += 1
            check_stack = []
        elif val != '0':
            check_stack.insert(0, val)
    if check_prime(int("".join(check_stack))):
        answer += 1
    return