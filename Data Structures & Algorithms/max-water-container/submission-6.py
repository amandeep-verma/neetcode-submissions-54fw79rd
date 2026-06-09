class Solution:
    def maxArea(self, heights: List[int]) -> int:

        # result= float("-inf")
        
        # for i in range(len(heights)):
        #     for j in range(i+1,len(heights)):
        #         vol = min(heights[i], heights[j]) * (j-i)
        #         result = max(result, vol)

        # return result

        result= -1
        left, right = 0 , len(heights)-1

        while right > left:
            vol = min(heights[left], heights[right]) * (right-left)
            result = max(result, vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result







