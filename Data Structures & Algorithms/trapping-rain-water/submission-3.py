class Solution:
    def trap(self, height: List[int]) -> int:
        
        maxRight = [0] * len(height)
        maxVal = -1

        for i in range(len(height)-1, -1, -1):
            maxRight[i] = maxVal
            
            maxVal = max(maxVal, height[i])

        totalWater = 0
        maxLeft = -1
        for i in range(len(height)):
            currVol = min(maxLeft, maxRight[i]) - height[i]

            if currVol> 0:
                totalWater = totalWater+ currVol

            maxLeft = max(maxLeft, height[i])

        return totalWater
        