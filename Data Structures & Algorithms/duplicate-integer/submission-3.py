class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        """Sol 1: Brute Force
        O(n*n) """
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        """Sol 2: Sort the array and see if 2 adjacent elements are same
        O(nlogn) """

        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False


        # myset= set()
        # for i in nums:
        #     if i in myset:
        #         return True
        #     myset.add(i)
        
        # return False
        