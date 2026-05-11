class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        myDict = defaultdict(int)

        for i in range(len(s)):
            myDict[s[i]] +=1
            myDict[t[i]] -=1

        for k,v in myDict.items():
            if v != 0:
                return False

        return True
            

        