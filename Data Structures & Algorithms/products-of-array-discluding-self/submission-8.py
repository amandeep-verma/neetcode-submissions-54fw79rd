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
        zeroIndex = []
        for i in range(len(nums)):
            if nums[i] ==0:
                zeroIndex.append(i)
                continue
            mul *= nums[i]

        # if len(zeroIndex) < 1:
        #     for j in range(len(nums)):
        #         res[j] = mul//nums[j]
        # elif len(zeroIndex) == 1:
        #     res[zeroIndex[0]] = mul
        #     return res

        if len(zeroIndex) < 2:

            for i, num in enumerate(nums):
                if zeroIndex: res[i] = 0 if i != zeroIndex[0] else mul
                else : res[i] = mul//num

            
        return res
