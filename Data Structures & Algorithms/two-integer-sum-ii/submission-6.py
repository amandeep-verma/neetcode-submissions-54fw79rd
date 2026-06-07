class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        myDict = defaultdict(int)

        for i in range(0, len(numbers)):
            comp = target - numbers[i]
            if comp in myDict:
                return [myDict.get(comp)+1, i+1 ]

            myDict[numbers[i]] = i
        