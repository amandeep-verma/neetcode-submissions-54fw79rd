class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
        Sol 1 Brute Force - check each number for every other number
        sort the array - sorting allows you to eliminate the duplicate triplet pairs
        n*n*n
        """

        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 tmp = [nums[i], nums[j], nums[k]]
        #                 res.add(tuple(tmp))
        # return list(list(x) for x in res)

        """
        Sol 2 - Sort the list and use the two sum sorted by using 2 left and right pointer but since
        the result cannot have duplicate numbers, we are eliminting it with checks or we could have 
        stored all pairs in a list and get rid of duplicates by 
        list(set(tuple(x) for x in res))
        n*n
        """

        # res = []
        # nums.sort()
        # for i, a in enumerate(nums):

        # # to avoid duplicates for the first index
        #     if i >0 and nums[i-1] == a:
        #         continue

        #     l, r = i+1 , len(nums) - 1
        #     while l < r:
        #         threeSum = a + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             r -= 1
        #             l += 1
            
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1

        # return res


        """
        Sol 3 - Use the hash - like we use to two sum.
        Sort the array 
        n*n
        """
        res = []
        nums.sort()
        mySet = {}
        for e in nums:
            if e not in mySet:
                mySet[e] = 0
            mySet[e] += 1

        for i in range(0, len(nums)):
            mySet[nums[i]] -= 1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i+1, len(nums)):
                mySet[nums[j]] -= 1

                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                target = -(nums[i] + nums[j])

                if mySet.get(target, 0) > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i+1, len(nums)):
                mySet[nums[j]] += 1
        
        return res 


