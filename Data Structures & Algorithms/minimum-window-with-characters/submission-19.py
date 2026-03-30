class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # """
        # Sol 1 brute force
        # Compare the entire dictionary of t and each substring of s with each other
        # O(n*n*m)
        # """

        # if len(t) > len(s):
        #     return ""

        # ss = ""
        # ssPresent = False

        # myDict1 = {}
        # myDict2 = {}
        # for i in range(len(t)):
        #     myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        # for i in range(0, len(s) - len(t) +1):
        #     myDict2 = {}

        #     for j in range(i, len(s)):
        #         myDict2[s[j]]= 1+ myDict2.get(s[j], 0)

        #         isMatch = True
        #         for key, val in myDict1.items():
        #             if myDict2.get(key, 0) < val:
        #                 isMatch = False

        #         if isMatch:
        #             if not ssPresent or (len(s[i:j+1]) < len(ss)):
        #                 ss = s[i:j+1]
                    
        #             ssPresent= True
        #             break
        # return ss

        # """
        # Sol 2 brute force - made better
        # Avoiding compare entire dictionary each time
        # O(n*n)
        # """

        # if len(t) > len(s):
        #     return ""

        # ss = ""
        # ssPresent = False

        # myDict1 = {}
        # myDict2 = {}
        # for i in range(len(t)):
        #     myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        # for i in range(0, len(s) - len(t) +1):

        #     # Notice if first character is not in dict1. it can not be shortest substring
        #     if s[i] not in myDict1:
        #         continue

        #     myDict2 = {}
        #     matchSet = set()

        #     for j in range(i, len(s)):
                
        #         myDict2[s[j]]= 1+ myDict2.get(s[j], 0)
        #         # Instead of comparing the entire dictionary each time, just compare the new element
        #         # and keep a count of it
        #         if s[j] not in matchSet and s[j] in myDict1 and myDict2[s[j]] >= myDict1[s[j]]:
        #             matchSet.add(s[j])

        #         if len(matchSet) == len(myDict1):
        #             if not ssPresent or (len(s[i:j+1]) < len(ss)):
        #                 ss = s[i:j+1]
                    
        #             ssPresent= True
        #             break
        # return ss

        """
        Sol 3 - better
        Avoiding compare entire dictionary each time
        O(n*n)
        """
        if len(t) > len(s):
            return ""

        myDict1 = {}
        myDict2 = {}
        for i in range(len(t)):
            myDict1[t[i]]= 1+ myDict1.get(t[i], 0)

        ss = ""
        matchSet = set()
        ssMaxL = float("inf")
        ssPresent = False

        l, r = 0, len(t)

        for r in range(len(s)):
            

            myDict2[s[r]] = myDict2.get(s[r],0) + 1

            if s[r] in myDict1 and myDict2[s[r]] >= myDict1[s[r]]:
                matchSet.add(s[r])

            while len(matchSet) == len(myDict1):
                if not ssPresent or len(ss)>len(s[l:r+1]):
                    ss = s[l:r+1]

                myDict2[s[l]] = myDict2.get(s[l]) -1

                if s[l] in myDict1 and myDict2[s[l]] < myDict1[s[l]]:
                    matchSet.remove(s[l])

                l += 1

                ssPresent = True

        return ss 










        

        for i in range(len(t)-1):
            myDict2[s[i]]= 1+ myDict2.get(s[i], 0)
        
        ss = ""
        l, r = 0, len(t)

        for r in range(len(t)-1, len(s)):

            myDict2[s[r]] = myDict2.get(s[r],0) +1

            match = True
            for key, val in myDict1.items():
                if val > myDict2.get(key, 0):
                    match = False
                    break
            
            while match and l <= r:
                
                if ss== "" or r-l+1 < len(ss):
                    ss = s[l:r+1]
                
                if myDict2[s[l]] == 1:
                    myDict2.pop(s[l])
                else:
                    myDict2[s[l]] -= 1
                l += 1
                
                for key, val in myDict1.items():

                    if val > myDict2.get(key, 0):
                        match = False
                        break

        return ss 



        