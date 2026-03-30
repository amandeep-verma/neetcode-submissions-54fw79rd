class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        """Solution 1 - make pairs of elements and frequency, Sort them and return the top k 
        n(log(n)) """

        # myDict = defaultdict(int)
        # for v in nums:
        #     myDict[v] += 1

        # # Add each key value in dict as a list of [value key] in new list, so we can sort them
        # myList = []
        # for key, value in myDict.items():
        #     myList.append([value,key])

        # myList.sort()
        
        # res = []
        # for i in range(len(myList)-k, len(myList)):
        #     res.append(myList[i][1])

        # return res


        """Solution 1a - exactly same as 1, but instead of list to sort, using dictionary itself 
        n(log(n)) """

        # myDict = defaultdict(int)
        # for v in nums:
        #     myDict[v] += 1

        # # Sorting the dictionary based on value
        # myDict = sorted(myDict.items(), key=lambda x:x[1])
        
        # res = []
        # for i in range(len(myDict)-k, len(myDict)):
        #     res.append(myDict[i][0])

        # return res

        """Solution 2 - using prirotyQueue 
        n(log(n))"""
        
        # myDict = defaultdict(int)

        # for v in nums:
        #     myDict[v] +=1
        
        # # Store the element in priorityQueue
        # heap = []

        # # Do we need to add elements in heapq. Insertion take log(n) time in heap. 
        # # Insertion of n item will take n log(n) time, We will make it better in Solution 2b
        # for key, v in myDict.items():
        #     heapq.heappush(heap, (v*-1, key))
        
        # result = []
        # for i in range(k):
        #     priority, task = heapq.heappop(heap)
        #     result.append(task)

        # return result

        """Solution 2b - using prirotyQueue but limiting the size of heap by k
        n(log(k))"""
        # myDict = defaultdict(int)

        # for v in nums:
        #     myDict[v] +=1
        
        # heap = []
        # # Limit the size of heap by size k
        # for key, v in myDict.items():
        #     heapq.heappush(heap, (v, key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)

        # result = []
        # while len(heap) > 0:
        #     result.append(heapq.heappop(heap)[1])

        # return result

        """Solution 2c - using prirotyQueue with heapify
        O(n) """
        
        # myDict = defaultdict(int)

        # for v in nums:
        #     myDict[v] +=1
        
        # # Instead of adding each elemement 1 by 1 in heap, convert dictionary in list and use heapify
        # # Underneath heapify use Floyd's Build-Heap alogrithm, which adds all element in O(n)
        # heap = [(-freq, key) for key, freq in myDict.items()]
        # heapq.heapify(heap)

        # result = []
        # for i in range(k):
        #     result.append(heapq.heappop(heap)[1])

        # return result

        """Solution 3 - using buckets
        O(n) """

        myDict = defaultdict(int)
        for v in nums:
            myDict[v] += 1

        bucket =[[] for i in range(len(nums) + 1)]
        for key, val in myDict.items():
            bucket[val].append(key)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result

        







        

        