# runtime: 450ms, memory: 14.1MB
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand_palindrome(left: str, right: str) -> str:
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
            return s[left+1:right]
        if(len(s) < 2 or s == s[::-1]):
            return s
        ret = ''
        for i in range(len(s)):
            ret = max(ret, expand_palindrome(i, i+1), expand_palindrome(i, i+2), key=len)
        return ret