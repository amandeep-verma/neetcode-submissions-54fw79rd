class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)

        # for i in range(len(nums)):
            
        #     for j in range(len(nums)):
        #         if i ==j:
        #             continue
        #         res[i] *= nums[j]


        # return res

        res = [0] * len(nums)
        mul = 1
        totalZero = 0
        index = -1
        for i in range(len(nums)):
            if nums[i] ==0:
                totalZero += 1
                index = i
                continue
            mul *= nums[i]

        if totalZero < 1:
            for j in range(len(nums)):
                res[j] = mul//nums[j]
        elif totalZero == 1:
            res[index] = mul
            return res
            
        return res
