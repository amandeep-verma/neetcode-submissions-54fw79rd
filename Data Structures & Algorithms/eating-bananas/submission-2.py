class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:


        """ 
        Sol 1 : Brute force - 
        Start with 1 and go to the highest number in the piles list 
        O (m*n) - where m is max number in piles
        """
        # for i in range(1,max(piles)):
        #     time = 0
        #     for j in range(len(piles)):
        #         time += math.ceil(piles[j]/i)
        #         # print(time)
        #     if time <= h:
        #         # print(time)
        #         return i

        # return max(piles)

        
        """
        Sol 2 - Binary Search 
        r = 1 , max(piles) - run binary search in this range

        1, 2, 3, 4
        """

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            m = l + (r-l)//2

            time = 0
            for pile in piles:
                time += math.ceil(pile/m)

            if time <= h:
                r = m-1
                res = m
            else:
                l = m+1

        return l
            

