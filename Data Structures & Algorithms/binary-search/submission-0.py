class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        first, last = 0, len(nums) -1

        while first <= last:
            mid = (int) ((first+last)/2)
            print(mid)
            if nums[mid] < target:
                first = mid +1
            elif nums[mid] > target:
                last = mid -1
            else:
                return mid

        return -1
