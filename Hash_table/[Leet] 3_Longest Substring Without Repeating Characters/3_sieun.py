# 시은 풀이 - 199ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 부분 문자열 최대 길이, 부분 문자열
        answer, substr = 0, ''
        
        for char in s:
            # 중복 x
            if char not in substr:
                substr += char
            # 중복 o
            else:
                # 현재 char 위치
                index = substr.index(char)
                # substr 갱신
                if index < len(substr) - 1:
                    substr = substr[index+1:] + char
                else:
                    substr = char
            # 최대 길이 갱신
            answer = max(answer, len(substr))
        
        return answer

# 교채 풀이 - 47ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 사용 문자
        used = {}
        # 최대 부분 문자열 길이, 부분 문자열 시작 인덱스
        answer, start = 0, 0
        
        for index, char in enumerate(s):
            # 이미 등장한 문자 -> start 위치 갱신
            if char in used and start <= used[char]:
                start = used[char] + 1
            # 최대 부분 문자열 길이 갱신
            else:
                answer = max(answer, index-start+1)
            # 현재 문자의 위치 갱신
            used[char] = index
            
        return answer