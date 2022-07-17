class Solution:
    def twoSum(self, nums, target):

        for vi, i in enumerate(nums):
            for vj, j in enumerate(nums[vi+1:]):
                if i+j == target:
                    return [vi, vi+vj+1]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
