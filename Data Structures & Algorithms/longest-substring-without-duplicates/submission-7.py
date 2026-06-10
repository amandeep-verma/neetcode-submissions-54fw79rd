class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        zxyzxyz
        



        """

        maxLength = 0

        for i in range(0, len(s)):

            for j in range(i+1, len(s)+1):

                subString = s[i:j+1]

                newSet = set()

                currLength = 0

                for c in subString:
                    if c in newSet:
                        currLength = 0
                        break
                    newSet.add(c)
                    currLength += 1
                
                maxLength = max(maxLength,currLength)

        return maxLength



        


            
