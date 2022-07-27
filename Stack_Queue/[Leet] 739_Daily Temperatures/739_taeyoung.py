# runtime: 2290, memory: 24MB
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for i, cur in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < cur:
                last = stack.pop()
                answer[last] = i-last
            stack.append(i)
        return answer