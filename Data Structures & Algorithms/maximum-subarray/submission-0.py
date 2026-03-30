class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        """

        2,-3,4,-2,2,1,-1,4 

        2 -3 4 -4 5 -5 



        """

        result = nums[0]

        currSum = nums[0]

        i, j = 0, 1

        while j< len(nums):

            currSum += nums[j]

            if nums[j] >= currSum:
                i =j
                currSum = nums[j]

            result = max(result, currSum)
            j=j+1

        return result

