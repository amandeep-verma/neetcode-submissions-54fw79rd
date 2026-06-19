class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        
        czxyzt
        012345



        """

        maxLength = 0
        l = 0
        myDict = {}

        for r, val in enumerate(s):

            if val in myDict and myDict[val]>= l:
                l = myDict.get(val) +1

            myDict[val] = r
            maxLength = max(maxLength, r-l +1)

        return maxLength






        


            
