class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        Sol 1 Brute force
        O(n)
        """

        # result = -1

        # for i, num in enumerate(nums):
        #     if num == target:
        #         return i

        # return result

        """
        Sol 2 Binary Search - Since array is sorted - use binary search
        O(log(n))
        """

        l, r =0, len(nums)-1
        
        while (l<= r):
            # Notice here (l+r) can lead to over flow
            mid = l+ (r-l)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid -1
            else:
                l= mid +1

        return -1

