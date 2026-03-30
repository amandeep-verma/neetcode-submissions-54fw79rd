class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l,r, = 0, len(nums)-1

        while l<=r:
            m = l + (r-l)//2

            if nums[m] < nums[0]:
                r = m -1
            else:
                l = m+1
        
        return nums[l] if l < len(nums) else nums[0]