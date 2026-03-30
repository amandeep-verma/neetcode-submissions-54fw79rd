class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Sol1 Brute force - For each index fidn the profit if selling at other index
        O(n*n)
        """

        """ Sol2 Brute force - For each index fidn the profit if selling at other index
        O(n*n)
        """
        

        
        minB = prices[len(prices) -2]
        maxS = prices[len(prices) -1]
        maxP = max(0,maxS - minB)

        for i in range (len(prices) -2, -1 , -1):
            
            minB = prices[i]
            maxP = max(maxP, maxS - minB)
            maxS = max( maxS, prices[i])
            print(maxP)


        return maxP





        