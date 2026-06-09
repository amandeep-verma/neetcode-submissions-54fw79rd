class Solution:
    def maxArea(self, heights: List[int]) -> int:

        
        result= float("-inf")
        
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                vol = min(heights[i], heights[j]) * (j-i)
                result = max(result, vol)

        return result



