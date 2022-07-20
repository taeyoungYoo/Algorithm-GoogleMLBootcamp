# Time limie exceeded
# O(n^3) and O(n^2 logn)
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         raw_ret = []
#         for i in range(len(nums)-2):
#             for j in range(i+1, len(nums)-1):
#                 for k in range(j+1, len(nums)):
#                     if(i != j and j != k and i != k and nums[i] + nums[j] + nums[k] == 0):
#                         raw_ret.append([nums[i], nums[j], nums[k]])
#         ret = []
#         for ans in raw_ret:
#             ans.sort()
#             if ans not in ret:
#                 ret.append(ans)
#         return ret
# runtime: 1294, memory: 18.1MB
# Two pointer method
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)-2):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = len(nums)-1
            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                if(sum == 0):
                    ret.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -=1
                    continue
                elif sum > 0:
                    right -= 1
                else:
                    left += 1
        return ret