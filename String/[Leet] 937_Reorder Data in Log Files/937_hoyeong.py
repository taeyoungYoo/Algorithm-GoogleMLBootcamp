class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        ㅇ log 타입
          -  Letter-logs : 영문 소문자
          - Digit-logs : 숫자
          
        ㅇ 규칙
          - letter 로그를 digit 로그 앞으로
          - letter 로그끼리는 컨텐츠의 알파벳 순서대로 (컨텐츠 처음도 같으면 구분자 순서대로) 
          - digit는 순서 유지한다.
        '''
        letters = []
        digits = []
        
        # 1번째 원소 기준으로 digit인지 letter인지 구분 
        for log in logs:
            if log.split()[1].isdigit(): # digit 추가
                digits.append(log)
            else:                        # letter 추가
                letters.append(log)
        
        # 정렬
        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        
        # 합치기
        return letters + digits
