class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)

        myList = [(-val, key) for key, val in counter.items()]

        heapq.heapify(myList)

        result = []

        for i in range(k):
            result.append(heapq.heappop(myList)[1])

        return result
