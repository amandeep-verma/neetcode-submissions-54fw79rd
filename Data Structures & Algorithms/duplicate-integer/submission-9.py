class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        mySet = set()

        for a in nums:
            if a in mySet:
                return True
            mySet.add(a)

        return False

        
        