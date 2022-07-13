# 시은 풀이 - 250ms
class Solution(object):
    def trap(self, height):
        n = len(height)

        # left[i]: max(height[:i])
        left = [height[0]] + [0 for _ in range(n - 1)]

        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])

        # right[i]: max(height[i+1:])
        right = [0 for _ in range(n - 1)] + [height[-1]]

        for i in reversed(range(0, n - 1)):
            right[i] = max(right[i + 1], height[i])

        # rain[i]: max(min(left[i], right[i]) - height[i], 0)
        rain = [max(min(left[i], right[i]) - height[i], 0) for i in range(n)]

        return sum(rain)

# 교재 풀이 - 168ms
class Solution2(object):
    def trap(self, height):
        result = 0
        stack = []

        for i in range(len(height)):
            # 변곡점을 만난 경우
            while stack and height[i] > height[stack[-1]]:
                # 변곡점의 높이
                top = stack.pop()

                if stack:
                    # 거리 차이
                    diff = i - stack[-1] - 1
                    # 물 높이
                    water = min(height[i], height[stack[-1]]) - height[top]
                    # 채우기
                    result += diff * water
            stack.append(i)

        return result
