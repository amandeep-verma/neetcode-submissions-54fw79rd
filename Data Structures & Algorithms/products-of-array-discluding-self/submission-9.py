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

        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n-1] = 1

        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n - 2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        print(pref)
        print(suff)

        for i in range(0,n):
            res[i] = pref[i] * suff[i]

        return res