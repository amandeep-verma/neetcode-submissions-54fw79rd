class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxP = 0

        maxSellPoint = [0] * len(prices)
        maxVal= 0
        for i in range (len(prices)-1, -1, -1):
            maxSellPoint[i]= maxVal
            maxVal = max(maxVal, prices[i])

            currP = maxSellPoint[i] - prices[i]
            maxP = max(maxP, currP)


        return maxP
