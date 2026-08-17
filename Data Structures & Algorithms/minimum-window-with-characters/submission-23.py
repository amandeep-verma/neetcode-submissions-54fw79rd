class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        myDict1 = {}
        myDict2 = {}
        for i in range(len(t)):
            myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        ss = ""
        have, need = 0 , len(myDict1)
        ssPresent = False
        l = 0

        for r in range(len(s)):

            myDict2[s[r]] = myDict2.get(s[r],0) + 1
            # Notice - increment happens when there is an exact match
            if s[r] in myDict1 and myDict2[s[r]] == myDict1[s[r]]:
                have += 1

            while have == need:
                if not ssPresent or len(ss)>(r+1-l):
                    ss = s[l:r+1]

                myDict2[s[l]] = myDict2.get(s[l]) -1

                if s[l] in myDict1 and myDict2[s[l]] < myDict1[s[l]]:
                    have -= 1

                l += 1

                ssPresent = True

        return ss 