class Solution:     # discuss, 교재 참고
    def longestPalindrome(self, s):

        if len(s) < 2 or s == s[::-1]:
            return s

        answer = s[0]

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        for i in range(len(s)):
            answer = max(answer, expand(i, i + 1), expand(i, i + 2), key=len)

        return answer


# 풀이1. : Time Limit Exceeded
# class Solution:
#     def longestPalindrome(self, s):
#         if len(s) < 2 or s == s[::-1]:
#             return s
#
#         palindrome = s[0]
#         for i in range(1, len(s)):
#             word = s[i - 1]
#             for j in s[i:]:
#                 word += j
#                 if word == word[::-1]:
#                     palindrome = max(palindrome, word, key=len)
#         return palindrome