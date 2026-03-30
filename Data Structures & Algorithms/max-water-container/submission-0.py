class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights)-1
        maxVol = 0

        while left<right:
            # print(f"left= {left} and right = {right}")
            l = heights[left]
            r = heights[right]

            currVol = (right - left) * (l if l < r else r)
            # print(f"curVol {currVol}")
            maxVol = currVol if currVol > maxVol else maxVol

            if r>l:
                left += 1
            elif l>r:
                right -= 1
            elif heights[left+1] > heights[right]:
                left += 1
            else:
                right -= 1

        return maxVol