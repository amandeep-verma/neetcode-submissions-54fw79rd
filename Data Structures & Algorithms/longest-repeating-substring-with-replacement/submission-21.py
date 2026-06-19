class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l, r = 0 , 0
        maxL = 0
        myDict = {}
        maxFreq = 0

        while r < len(s):

            myDict[s[r]] = myDict.get(s[r], 0) +1

            diffChar = sum(myDict.values()) - max(myDict.get(s[r]), maxFreq)
            maxFreq = max(myDict.get(s[r]), maxFreq)
            # diffChar = (r- l +1) - maxFreq

            while diffChar > k:

                myDict[s[l]] -= 1
                l += 1 

                diffChar = sum(myDict.values()) - max(myDict.get(s[r]), maxFreq)
                # diffChar = (r- l +1) - maxFreq

            maxL = max(maxL, r-l +1)

            r += 1

        return maxL





"""
AAABABBBBBB

A: 4
B: 1


xyzzxyz k = 2

zzxyz


"""