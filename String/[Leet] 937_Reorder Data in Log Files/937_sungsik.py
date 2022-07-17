class Solution:
    def reorderLogFiles(self, logs):

        logs_let = []   # 빈 letter-logs list 생성
        logs_dig = []   # 빈 digit-logs list 생성

        for log in logs:    # 전체 log에 대해 분류작업
            try:
                content = int(log.split(' ')[1])    # 구분자를 제외한 첫 번째 content가 int일 경우
                logs_dig.append(log)                # digit-logs list에 추가
            except:
                logs_let.append(log)                # 아닐 경우 letter-logs list에 추가

        logs_let = [x.split(' ') for x in logs_let]     # letter-logs를 정렬하기 위해 공백 기준으로 2차원 리스트화
        logs_let = sorted(logs_let, key=lambda x: (x[1:], x[0]))    # letter-logs를 content, id 순서의 다중조건을 기준으로 정렬
        logs_let = [' '.join(x) for x in logs_let]      # 2차원 리스트를 다시 1차원 리스트로 변환

        return logs_let + logs_dig      # letter-logs list와 digit-logs list를 합쳐서 반환


logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
print(Solution().reorderLogFiles(logs))
