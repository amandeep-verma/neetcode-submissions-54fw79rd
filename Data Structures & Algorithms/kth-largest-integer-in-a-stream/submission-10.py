class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        """
        Sol 1 using min heap
        we create a min heap and ensure the size is k. The minimum element here is kth largest element in array
        m log(k) - where m is number of times add function is called
        """
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) >k:
            heapq.heappop(self.minHeap)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
        
