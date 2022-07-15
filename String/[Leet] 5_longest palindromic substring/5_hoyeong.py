class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        어렵다 책보고 풀이진행
        패드로 그리면서 다시 풀어볼 것
        
        ㅇ 풀이법
          1) 부르트포스 : 시간 복잡도 O(n^3) -> O(n) * O(n^2) (탈락)
             b / ba / bab / baba / babad
             a / ab / aba / abad
          2) 포인터 이용 : 시간 복잡도 O(n) * O(n) -> O(n^2)
        -    b / bab / babad / bad / d
        '''
        
        # 팰린드롬 판별 및 포인터(left, right) 확장 함수
        def expand(l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1 :r]  # l -= 1 을 했기 때문에 l+1을 한다
        
        # 예외처리
        # s의 길이가 2미만 이거나, s 자체가 팰린드롬 일 때 바로 리턴
        if len(s) < 2 or s == s[::-1]:
            return s
        
        res = ''
        
        for i in range(len(s) -1):
            res = max(res, expand(i, i+1), expand(i, i+2), key=len)   # 책 풀이
            # res = max(res, expand(i, i), expand(i, i+1), key=len)   # youtube 풀이 (어떤 차이?)
        
        return res
