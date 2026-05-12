class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # count = Counter(nums)

        # count= sorted(count.items(), key = lambda x : -x[1])

        # print(count)
        # print(type(count))

        # return [count[i][0] for i in range(0,k)]

        myDict = defaultdict(int)

        for num in nums:
            myDict[num] +=1

        freqArray = [[] for i in range(len(nums)+1)]

        for key, val in myDict.items():
            freqArray[val].append(key)

        result = []
        for i in range(len(freqArray)-1, 0, -1):
            for num in freqArray[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
        return result
