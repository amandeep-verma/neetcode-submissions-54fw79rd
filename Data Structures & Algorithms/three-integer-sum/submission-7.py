class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        resultSet = set()

        # n*n * 3 log 3
        for i in range(len(nums)):

            mySet= set()

            for j in range(i+1,len(nums)):

                comp = -1 * (nums[i] + nums[j])

                if comp in mySet:
                    anotherList = [nums[i], comp, nums[j]]
                    anotherList.sort()
                    # print(anotherList)
                    
                    resultSet.add(tuple(anotherList))

                mySet.add(nums[j])

        for v in resultSet:
            result.append(list(v))

        return result
