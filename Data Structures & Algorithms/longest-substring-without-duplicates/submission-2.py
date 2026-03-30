class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        myDict = {}
        maxLength = 0

        tempStart = 0

        for i, val in enumerate(s):
            if val in myDict and myDict[val] >= tempStart:
                tempStart = myDict[val] +1

            myDict[val] = i



            maxLength = max(maxLength, i- tempStart +1)
        

        return maxLength
        