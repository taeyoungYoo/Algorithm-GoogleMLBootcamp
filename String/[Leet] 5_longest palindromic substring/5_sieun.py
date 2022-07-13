# 시은 풀이 - 시간 초과
class Solution(object):
    def longestPalindrome(self, s):
        n, maxWord = len(s), s[0]

        for i in range(n):
            for j in range(i + len(maxWord) + 1, n + 1):
                word = s[i:j]
                if word == word[::-1]:
                    maxWord = word

        return maxWord

# 교재 풀이 - 328ms
class Solution2(object):
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''

        # 슬라이딩 윈도우 우측으로 이동
        for i in range(len(s) - 1):
            result = max(result,
                         self.expand(s, i, i + 1),
                         self.expand(s, i, i + 2),
                         key=len)

        return result
