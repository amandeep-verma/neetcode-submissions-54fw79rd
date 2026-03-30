class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # if len(t) > len(s):
        #     return ""

        # myDict1 = {}
        # myDict2 = {}
        # for i in range(len(t)):
        #     myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        # for i in range(len(t)-1):
        #     myDict2[s[i]]= 1+ myDict2.get(s[i], 0)
        
        # ss = ""
        # l, r = 0, len(t)

        # for r in range(len(t)-1, len(s)):

        #     myDict2[s[r]] = myDict2.get(s[r],0)+1

        #     match = True
        #     for key, val in myDict1.items():
        #         if val > myDict2.get(key, 0):
        #             match = False
        #             break
            
        #     while match and l<= r:
                
        #         if ss== "" or r-l+1 < len(ss):
        #             ss = s[l:r+1]
                
        #         if myDict2[s[l]] == 1:
        #             myDict2.pop(s[l])
        #         else:
        #             myDict2[s[l]] -= 1
        #         l += 1
                
        #         for key, val in myDict1.items():

        #             if val > myDict2.get(key, 0):
        #                 match = False
        #                 break

        # return ss 

        """
        Sol 1 brute force
        compare sorted s1 with sorted subtring of s2
        O(n*n)
        """

        if len(t) > len(s):
            return ""

        ss = ""
        ssPresent = False

        myDict1 = {}
        myDict2 = {}
        for i in range(len(t)):
            myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        for i in range(0, len(s) - len(t) +1):
            myDict2 = {}

            for j in range(i, len(s)):
                myDict2[s[j]]= 1+ myDict2.get(s[j], 0)

                isMatch = True
                for key, val in myDict1.items():
                    if myDict2.get(key, 0) < val:
                        isMatch = False

                if isMatch:
                    if not ssPresent or (len(s[i:j+1]) < len(ss)):
                        ss = s[i:j+1]
                    
                    ssPresent= True
                    break
        return ss




        """

        """
        