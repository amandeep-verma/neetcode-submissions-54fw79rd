class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        """Solution 1 - convert """

        myDict = defaultdict(int)
        for v in nums:
            myDict[v] += 1

        # Add each key value in dict as a list of [value key] in new list, so we can sort them
        # myList = []
        # for key, value in myDict.items():
        #     myList.append([value,key])

        # myList.sort()

        myList = sorted(myDict.items(), key=lambda x:x[1])
        
        res = []
        for i in range(len(myList)-k, len(myList)):
            res.append(myList[i][0])

        return res


        # sortedDict = sorted(myDict.items(), key=lambda x:x[1])



        
        # result = []

        # # Store the element in priorityQueue
        # heap = []

        # myDict = defaultdict(int)

        # for v in nums:
        #     myDict[v] +=1
        
        # # Since 
        # for key, v in myDict.items():
        #     heapq.heappush(heap, (v*-1, key))
        
        # for i in range(k):
        #     priority, task = heapq.heappop(heap)
        #     result.append(task)

        # return result