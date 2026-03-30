class Solution:

    def trap(self, height: List[int]) -> int:

        """ Sol 1 Brute force - for each index find max Right and max Left one by one
        O(n*n)
        """

        """ Sol 2 Create a list of maxLeft and maxRight and compute it in one go
        O(n)
        """
        # maxLeft = []
        # maxRight = [0] * len(height)
        # maxL = 0
        # maxR = 0
        # for i in range(len(height)):
        #     maxLeft.append(maxL)
        #     maxRight[len(height) - 1- i] = maxR
        #     maxL = max(height[i], maxL)
        #     maxR = max(height[len(height) - 1- i], maxR)

        # totalWater = 0
        # for i in range(len(height)):
        #     currWat = min(maxLeft[i],maxRight[i]) - height[i]
        #     totalWater = totalWater if currWat < 0 else totalWater + currWat
        # return totalWater


        """ Sol 3 two pointer approach. No extra lists needed
        Start from left and right, move the side which is smaller, use the max of that side to determine
        the water. 
        O(n)
        """

        l, r = 0, len(height) -1
        maxL = height[l]
        maxR = height[r]
        totalWater = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                maxL = max(maxL, height[l])
                totalWater += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                totalWater += maxR - height[r]

        return totalWater

        