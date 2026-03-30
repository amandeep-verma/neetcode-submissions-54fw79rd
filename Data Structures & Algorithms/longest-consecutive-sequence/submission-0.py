class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """ Sol 1 brute force
        n*n """ 


        """ Sol 2 
        O(n) """ 
        
        mySet = set(nums)
        maxLength = 0

        starterOfSeries = []
        
        for num in mySet:
            if (num - 1) in mySet:
                continue
            starterOfSeries.append(num)

        for v in starterOfSeries:
            currMaxLength = 1
            nextNum = v+1
            while nextNum in mySet:
                currMaxLength += 1
                nextNum += 1
            if currMaxLength > maxLength:
                maxLength = currMaxLength

        return maxLength;
