# 시은 풀이 - 40ms
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 알고리즘 함수 
        def get_combs(i=0, comb=''):
            if i == len(digits):
                return answer.append(comb) 
            
            for letter in letters[digits[i]]:
                get_combs(i+1, comb+letter)
        
        # 빈 문자열 -> 조합 x
        if len(digits) == 0:
            return []
        
        # 숫자-영문 map
        letters = {'2': ['a', 'b', 'c'],
                   '3': ['d', 'e', 'f'],
                   '4': ['g', 'h', 'i'],
                   '5': ['j', 'k', 'l'],
                   '6': ['m', 'n', 'o'],
                   '7': ['p', 'q', 'r', 's'],
                   '8': ['t', 'u', 'v'],
                   '9': ['w', 'x', 'y', 'z']}
        
        answer = []
        get_combs()        
        return answer