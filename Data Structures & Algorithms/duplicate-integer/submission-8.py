class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # Brute Force -1 
        # # O(n*n)
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
                
        #         if nums[i] ==nums[j]:
        #             return True
        # return False

        # Brute Force sorted 
        # O(nlogn)
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                return True

        return False

        
        