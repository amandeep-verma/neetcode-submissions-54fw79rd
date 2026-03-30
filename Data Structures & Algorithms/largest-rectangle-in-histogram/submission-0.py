class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Sol 1: Brute force
        O(n*n)
        """
        maxArea = 0

        for i in range(len(heights)):
            minHeight = float('inf')

            for j in range(i, len(heights)):
                

                width = j-i+1
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight* width)

        return maxArea

