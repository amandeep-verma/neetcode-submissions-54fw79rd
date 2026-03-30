class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        mySet = set()
        myDict = {}
        maxLength = 0

        l = 0
        tempMaxRep = 0 

        for i, val in enumerate(s):

            myDict[val] = 1+ myDict.get(val, 0)
            
            while i- l +1 - max(myDict.values()) > k and l < len(s):
                myDict[s[l]] -= 1
                l += 1
            
            maxLength = max(maxLength, i- l +1)
        

        return maxLength