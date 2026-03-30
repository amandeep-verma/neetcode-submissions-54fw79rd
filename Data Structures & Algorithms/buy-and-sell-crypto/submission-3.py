class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Sol1 Brute force - For each index fidn the profit if selling at other index
        O(n*n)
        """

        """ Sol2 Brute force - For each index fidn the profit if selling at other index
        O(n*n)
        """
        
        maxS = prices[len(prices) -1]
        maxP = 0

        for i in range (len(prices) -2, -1 , -1):
            buyingPrice = prices[i]
            maxP = max(maxP, maxS - buyingPrice)
            maxS = max( maxS, prices[i])

        return maxP





        