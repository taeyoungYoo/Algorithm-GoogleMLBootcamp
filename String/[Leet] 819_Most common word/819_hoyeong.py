class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        '''
        - 가장 많이 출연한 단어 출력
        - 금지어(banned)에 없는 단어
        - 소문자로 출력
        
        ㅇ 접근법
        - "!?',;." 제거 필요 (정규식표현으로 제거)
        - 소문자 변환 필요(매번? 한번에?)
        - banned에 있는 단어는 예외처리
        - counter 메서드로 딕셔너리 생성 후 빈도가 가장 큰 key값 출력
        
        ㅇ 새로배운 점
        - max() 에도 key를 이용할 수 있다.
        - re.sub(r'[^\w]', ' ', paragraph) -> paragraph 안에서 word character가 아닌경우 공백으로 변경
          - \W -> Word character
          - ^ -> not
        - .most_common(n) 가장 빈도가 높은 n개의 요소 반환
        '''        
        
        words = [ w for w in re.sub(r'[^\w]', ' ', paragraph)    # 1. - "!?',;." 제거
                    .lower().split()                            # 2. 소문자 변환
                    if w not in banned ]                         # 3. banned에 있는 단어 제거
    
        # 4. 빈도 계산 및 출력
        counts = collections.Counter(words)
        return counts.most_common(n=1)[0][0]
