class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0
        maxSellingPrice = 0

        for i in range (len(prices)-1, -1, -1):
            maxSellingPrice = max(maxSellingPrice, prices[i])
            
            maxP = max(maxP, maxSellingPrice - prices[i])

        return maxP
