class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []
        def combination(elements: list, start: int, cnt: int):
            if cnt == k:
                ret.append(elements[:])
                return

            for i in range(start, n + 1):
                elements.append(i)
                combination(elements, i + 1, cnt + 1)
                elements.pop()


        combination([], 1, 0)
        return ret