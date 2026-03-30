class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Sol1 Brute force - For each index fidn the profit if selling at other index
        O(n*n)
        """

        """ Sol2 
        You can sell only after buying. In order to make maxProfit, you need to sell at highest price
        and buy at lowest. Again, you sell only after buying.
        Keep a track a min from current index and iterate through the list. Sell at current index.
        Profit is SellingPrice at current index - minBuyPriceSoFar
        O(n)
        """
        
        # maxS = prices[len(prices) -1]
        # maxP = 0

        # for i in range (len(prices) -2, -1 , -1):
        #     buyingPrice = prices[i]
        #     maxP = max(maxP, maxS - buyingPrice)
        #     maxS = max( maxS, prices[i])

        # return maxP

        minBuyingPrice = prices[0]
        maxP = 0

        for val in prices:
            maxP = max(maxP, val - minBuyingPrice)
            minBuyingPrice = min(minBuyingPrice, val)

        return maxP




        