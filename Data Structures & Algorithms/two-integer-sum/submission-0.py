class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for i,v in enumerate(nums):
            
            compliment = target - v
            if compliment in myDict:
                return [myDict[compliment], i]
            myDict[v]=i

        return []

            


        