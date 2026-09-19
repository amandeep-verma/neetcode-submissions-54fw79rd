class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap= [-a for a in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)

            res = b - a
            heapq.heappush(heap, -res)

        return -heap[0]

