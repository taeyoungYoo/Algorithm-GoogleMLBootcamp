import re


class Solution:
    def isPalindrome(self, s: str):

        s = re.sub("[^a-z0-9]",'',s.lower())    # input을 정규표현식을 사용해 알파벳과 숫자만 남김

        return True if s == s[::-1] else False  # s와 s를 뒤집은 문자열이 같은지 비교


s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
