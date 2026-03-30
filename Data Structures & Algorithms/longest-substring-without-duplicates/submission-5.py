class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0 , 0

        myDict = {}
        maxL = 0

        while r < len(s):

            if s[r] in myDict and l <= myDict[s[r]]:
                l = myDict[s[r]]+1
            
            myDict[s[r]] = r
            maxL = max(maxL, r-l+1)
            print(maxL, r, l)
            r = r+1

        return maxL
            
