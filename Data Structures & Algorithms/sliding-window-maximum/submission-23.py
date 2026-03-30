class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        """
        Sol 1 brute force
        Iterate through the list and check for max in each subArray
        O(n*k)
        """

        # result = []
        # for i in range(0, len(nums)-k +1):
        #     result.append(max(nums[i:i+k]))

        # return result

        """
        Sol 2 - using sliding window
        Avoiding compare entire dictionary each time. Rather keeping a count of match
        O(n)
        """
        myDict = {}
        heap = [-num for num in nums[0:k]]

        heap = [(-nums[i],i) for i in range(0,k)]

        heapq.heapify(heap)


        result = [-heap[0][0]]

        
        for i in range(k, len(nums)):
            heapq.heappush(heap,(-nums[i],i))

            while heap[0][1] < i-k+1:
                heapq.heappop(heap)
            
            result.append(-heap[0][0])

        return result