# Get the volume using max operation on every point of height
# max(list) = O(n)
# O(n^2) -> TLE
class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)-1):
            l_max = max(height[:i])
            r_max = max(height[i:])
            if(l_max < height[i] or r_max < height[i]):
                continue
            water += min(l_max, r_max) - height[i]
        return water

# 책 코드
# runtime: 256ms, memory: 16.1
class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        left, right = 0, len(height)-1
        left_max = height[left]
        right_max = height[right]
        while left < right: # max에 도달하기 전
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume