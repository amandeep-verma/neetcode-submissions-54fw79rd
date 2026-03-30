class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """Solution 1 - Brute force - for each element - find the product of all other elements
        Can be made better by if any number 0, the product will be 0
        O(n*n) """


        """Solution 2 - Find the product of all elements. Use product as constant and divide it by 
        each element 1 by 1 and find the remaining product
        Edge case - When there is 1 zero in the list - All other index will have product as 0 other than 
        zero index itself. But when there is more than 1 zero and output elements will be 0
        O(n*n) """

        product=1
        zeroIndexes = []
        for i,num in enumerate(nums):
            if num == 0:
                zeroIndexes.append(i)
                continue
            product *= num

        res = [0]*len(nums)

        if len(zeroIndexes) > 1:
            return res
        elif len(zeroIndexes) == 1:
            for i,num in enumerate(nums):
                nums[i] = product if i == zeroIndexes[0] else 0
        else:
            for i,num in enumerate(nums):
                nums[i] = product//num

        return nums
        