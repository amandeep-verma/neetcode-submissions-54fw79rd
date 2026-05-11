class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myDict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in myDict:
                return [myDict[comp], i]
            
            myDict[nums[i]] = i
            