class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        Sol 1 Brute Force - check each number for every other number
        n*n*n
        """

        # res = []
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.append(tmp)
        # return list(set(tuple(x) for x in res))

        """
        Sol 2 - Sort the list and use the two sum sorted by using 2 left and right pointer but since
        the result cannot have duplicate numbers 
        n*n
        """

        res = []
        nums.sort()
        for i, a in enumerate(nums):

        # to avoid duplicates for the first 
            if i >0 and nums[i-1] == a:
                continue

            l, r = i+1 , len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1

        # You can not add list to set, so converting each list to tuple, to add to set and later convert
        # to list
        return list(set(tuple(x) for x in res))

