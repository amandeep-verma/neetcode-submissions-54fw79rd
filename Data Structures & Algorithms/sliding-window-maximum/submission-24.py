class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        

        """

        1,2,1,1,1,0,4,2,6

        -1:0, -2:1, -1:2, -1:3, -1:4


        res = [2, 2, ]




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
        Use max heap to keep the numbers and as you iterating, look for the top number. If the index is less than 
        the start of block - pop it else append it to result
        O(n logn)
        """
        # myDict = {}
        # # heap = [-num for num in nums[0:k]]

        # heap = [(-nums[i],i) for i in range(0,k)]

        # heapq.heapify(heap)
        # result = [-heap[0][0]]

        # for i in range(k, len(nums)):
        #     heapq.heappush(heap,(-nums[i],i))

        #     while heap[0][1] < i-k+1:
        #         heapq.heappop(heap)
            
        #     result.append(-heap[0][0])

        # return result


        """
        # Sol 3 - using deque
        # Use a deque to store indices of elements in the current window.
        # Monotonic deque
        """

        output = []
        q = deque()  # index
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1

        return output