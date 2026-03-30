class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        myArr = [0] * 26

        for i in range(len(s)):
            myArr[ord(s[i])- 97] += 1
            myArr[ord(t[i])- 97] -= 1

        for o in myArr:
            if o != 0:
                return False
        return True


        