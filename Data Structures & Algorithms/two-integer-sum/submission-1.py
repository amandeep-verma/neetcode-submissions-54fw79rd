class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        myDict = defaultdict(list)

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in myDict:
                return [myDict.get(diff)[0], i]

            myDict[nums[i]].append(i)