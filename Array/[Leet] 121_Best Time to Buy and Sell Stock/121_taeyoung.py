# runtime: 2232ms, memory: 25.1MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret_min = max(prices)
        ret_max = 0

        for price in prices:
            ret_min = min(price, ret_min)
            ret_max = max(ret_max, price - ret_min)
        return ret_max