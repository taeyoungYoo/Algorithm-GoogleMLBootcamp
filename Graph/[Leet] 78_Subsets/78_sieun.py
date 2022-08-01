from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        
        for i in range(len(nums)+1):
            answer += list(combinations(nums, i))
        
        return answer