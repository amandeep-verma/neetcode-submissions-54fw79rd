class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        mySet = set()
        myDict = {}
        maxLength = 0
        l = 0

        for r, val in enumerate(s):

            myDict[val] = 1+ myDict.get(val, 0)
            
            maxVal = max(myDict.values())
            while r- l +1 - maxVal > k :
                myDict[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r- l +1)
        

        return maxLength