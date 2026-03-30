class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zeroIndexes = []
        for i,num in enumerate(nums):
            if num == 0:
                zeroIndexes.append(i)
                continue
            product *= num

        
        if len(zeroIndexes) > 1:
            return [0]*len(nums)
        elif len(zeroIndexes) == 1:
            for i,num in enumerate(nums):
                if i == zeroIndexes[0]:
                    nums[i] = product
                else:
                    nums[i]=0
            return nums
        else:
            for i,num in enumerate(nums):
                nums[i] = product//num

        return nums
        