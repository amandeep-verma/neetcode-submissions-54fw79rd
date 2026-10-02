import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort()
        self.arr = nums
        self.size = k
        
        
    def add(self, val: int) -> int:

        index = bisect.bisect_left(self.arr, val)
        self.arr.insert(index, val)

        if len(self.arr) > self.size:
            self.arr = self.arr[len(self.arr) - self.size-1 :]

        print(self.arr)
        return self.arr[- self.size]