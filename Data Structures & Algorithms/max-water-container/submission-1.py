class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Sol 1 Brute Force - check each index for every other index
        O(n*n)
        """
        maxVol = 0

        for i in range(0, len(heights)):

            for j in range(i+1, len(heights)):
                currVol = (j - i) * (heights[i] if heights[i] < heights[j] else heights[j])
                maxVol = currVol if currVol > maxVol else maxVol

        return maxVol

        
        # left, right = 0, len(heights)-1
        # maxVol = 0

        # while left<right:
        #     l = heights[left]
        #     r = heights[right]

        #     currVol = (right - left) * (l if l < r else r)
        #     maxVol = currVol if currVol > maxVol else maxVol

        #     if r>l:
        #         left += 1
        #     elif l>r:
        #         right -= 1
        #     elif heights[left+1] > heights[right]:
        #         left += 1
        #     else:
        #         right -= 1

        # return maxVol