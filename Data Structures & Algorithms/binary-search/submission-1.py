class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        Sol 1 Brute force
        O(n)
        """

        result = -1

        for i, num in enumerate(nums):
            if num == target:
                return i

        return result