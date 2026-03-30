class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = [0] * len(height)
        maxL = 0
        maxR = 0
        for i in range(0, len(height)):
            maxLeft.append(maxL)
            maxRight[len(height) - 1- i] = maxR
            maxL = height[i] if maxL < height[i] else maxL
            maxR = height[len(height) - 1- i] if maxR < height[len(height) - 1- i] else maxR

        totalWater = 0
        for i, v in enumerate(height):
            currWat = min(maxLeft[i],maxRight[i]) - height[i]
            totalWater = totalWater if currWat < 0 else totalWater + currWat
        return totalWater
        