class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = [0] * len(height)
        maxL = 0
        maxR = 0
        for i in range(len(height)):
            maxLeft.append(maxL)
            maxRight[len(height) - 1- i] = maxR
            maxL = max(height[i], maxL)
            maxR = max(height[len(height) - 1- i], maxR)

        totalWater = 0
        for i in range(len(height)):
            currWat = min(maxLeft[i],maxRight[i]) - height[i]
            totalWater = totalWater if currWat < 0 else totalWater + currWat
        return totalWater
        