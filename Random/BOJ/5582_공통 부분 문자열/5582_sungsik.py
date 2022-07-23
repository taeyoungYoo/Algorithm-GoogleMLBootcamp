s1 = 'ABRACADABRA'
s2 = 'ECADADABRBCRDARA'


# 입력받은 문자열 s1과 s2의 길이를 비교해서 short와 long으로 구분
if len(s1) <= len(s2):
    short, long = s1, s2
else:
    short, long = s2, s1

p1 = 0      # 부분 문자열 슬라이싱할 포인터
p2 = 1
answer = 0

while p2 < len(short):      # short의 문자열 끝까지 탐색

    sub_s = short[p1:p2]    # 체크할 부분 문자열

    if sub_s in long:                       # 공통 부분 문자열이 있으면
        answer = max(answer, len(sub_s))    # 길이를 비교해서 answer 갱신
        p2 += 1                             # 포인터2 오른쪽으로 한칸 이동
    else:
        p1 += 1                             # 부분 문자열이 없으면 포인터1 오른쪽으로 한칸 이동

print(answer)
# 메모리 : 30840 kb,  시간: 2828 ms
