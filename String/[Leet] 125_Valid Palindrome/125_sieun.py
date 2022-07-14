# 35ms
class Solution(object):
    def isPalindrome(self, s):
        # 변환
        s = re.sub(r'[^A-Z0-9]', '', s.upper())
        # 비교
        return s == s[::-1]