class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        myDict = {}
        maxLength = 0

        tempStart = -1

        for i, val in enumerate(s):
            if val in myDict and myDict[val] >= tempStart:
                tempStart = myDict[val] 

            myDict[val] = i
            maxLength = max(maxLength, i- tempStart )


        return maxLength
        