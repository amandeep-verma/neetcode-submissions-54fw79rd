class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []

        # Store the element in priorityQueue
        pq = []

        myDict = defaultdict(int)

        for v in nums:
            myDict[v] +=1
        
        for key, v in myDict.items():
            heapq.heappush(pq, (v*-1, key))
        
        for i in range(k):
            print(i)
            priority, task = heapq.heappop(pq)
            result.append(task)

        return result