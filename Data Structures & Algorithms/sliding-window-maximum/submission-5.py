class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        myDict = {}
        heap = [-num for num in nums[0:k-1]]

        heapq.heapify(heap)

        for i in range(k-1):
            myDict[nums[i]] = myDict.get(nums[i], 0) + 1

        result = []

        
        for i in range(k-1, len(nums)):
            myDict[nums[i]] = myDict.get(nums[i], 0) + 1
            heapq.heappush(heap,-nums[i])

            if i - k >=0:
                if myDict.get(nums[i-k], 0) < 2:
                    myDict.pop(nums[i-k])
                else:
                    myDict[nums[i-k]] = myDict.get(nums[i-k], 0) - 1
            # print(i," ",myDict," ",[-e for e in heap])

            while myDict.get(-heap[0], 0) < 1:
                heapq.heappop(heap)
            
            smallest = -heap[0]

            # if i - k >=0:
            #     if nums[i-k] in heap:
            #         print(f"{nums[i-k]} yes it is there")
            #         heap.remove(nums[i-k])
            #         heapq.heapify(heap)

            # print(smallest)
            result.append(smallest)

        return result

"""
1,2,1,0,4,2,6

  2 1 0

1: 1, 2: 1, 0: 1

2, 1, 1, 0

2

"""



