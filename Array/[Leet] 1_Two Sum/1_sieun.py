# 시은 풀이 - 2395ms
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 시은 풀이(교재 참고) - 382ms
class Solution2(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            num1, num2 = nums[i], target-nums[i]
            if num2 in nums[i+1:]:
                j = nums[i+1:].index(num2) + i + 1
                return [i, j]

# 교재 풀이 - 84ms
class Solution3(object):
    def twoSum(self, nums, target):
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i
