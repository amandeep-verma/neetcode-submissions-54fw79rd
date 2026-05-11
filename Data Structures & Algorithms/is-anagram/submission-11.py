class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        myDict = {}
        for i in range(0,26):
            myDict[chr(ord('a')+(i))] = 0

        for i in range(len(s)):
            myDict[s[i]] +=1
            myDict[t[i]] -=1

        for k,v in myDict.items():
            if v != 0:
                return False

        return True
            

        