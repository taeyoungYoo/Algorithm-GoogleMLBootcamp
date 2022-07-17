# runtime: 69ms, memory: 14.8MB
# Two pointer to check the target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0;
        right = len(nums)-1
        sort_num = sorted(nums)
        while(left <= right):
            tmp = sort_num[left] + sort_num[right]
            if tmp == target:
                break
            elif tmp > target:
                right -= 1
            elif tmp < target:
                left += 1
        ret_left = nums.index(sort_num[left])
        ret_right = nums.index(sort_num[right])
        if ret_left == ret_right:
            duplicate = list(filter(lambda x:nums[x] == sort_num[right], range(len(nums))))
            ret_left = duplicate[0]
            ret_right = duplicate[1]
        return [ret_left, ret_right]