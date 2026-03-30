class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        myDict = {}
        heap = [-num for num in nums[0:k]]

        heapq.heapify(heap)

        for i in range(k):
            myDict[nums[i]] = myDict.get(nums[i], 0) + 1

        result = [-heap[0]]

        
        for i in range(k, len(nums)):
            myDict[nums[i]] = myDict.get(nums[i], 0) + 1
            heapq.heappush(heap,-nums[i])

            myDict[nums[i-k]] = myDict.get(nums[i-k], 0) - 1
            # print(i," ",myDict," ",[-e for e in heap])

            while myDict.get(-heap[0], 0) < 1:
                heapq.heappop(heap)
            
            result.append(-heap[0])

        return result

"""
1,2,1,0,4,2,6

  2 1 0

1: 1, 2: 1, 0: 1

2, 1, 1, 0

2

"""



