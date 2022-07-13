# 시은 풀이 - 4298ms
class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()

        for i, num1 in enumerate(nums):
            # 중복 케이스 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            nums_map = {}
            # twoSum 활용
            for j, num2 in enumerate(nums[i + 1:]):
                target = - (num1 + num2)
                triplets = [num1, num2, target]
                if target in nums_map and triplets not in result:
                    result.append(triplets)
                nums_map[num2] = j

        return result


# 교재 풀이 - 1005ms
class Solution2(object):
    def threeSum(self, nums):
        n = len(nums)
        result = []
        nums.sort()

        for i in range(n - 2):
            # 중복 케이스 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 투포인터
            left, right = i + 1, n - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    # 정답 추가
                    result.append([nums[i], nums[left], nums[right]])
                    # 중복 케이스 제거
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result