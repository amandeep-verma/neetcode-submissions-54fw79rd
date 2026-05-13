class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = [1] * len(nums)

        # for i in range(len(nums)):
            
        #     for j in range(len(nums)):
        #         if i ==j:
        #             continue
        #         res[i] *= nums[j]


        # return res

        # res = [0] * len(nums)
        # mul = 1
        # zeroIndex = []
        # for i in range(len(nums)):
        #     if nums[i] ==0:
        #         zeroIndex.append(i)
        #         continue
        #     mul *= nums[i]

        # if len(zeroIndex) < 1:
        #     for j in range(len(nums)):
        #         res[j] = mul//nums[j]
        # elif len(zeroIndex) == 1:
        #     res[zeroIndex[0]] = mul
        #     return res

        # return res

        n = len(nums)

        res = [1] * (len(nums))

        prefix = res[1]= 1
        for i in range(1, len(nums)):
            res[i] = res[i-1]* nums[i-1]
        
        suffix = 1

        for i in range(n-1, -1, -1):
            res[i] = res[i] * suffix
            suffix *= nums[i]

        return res



