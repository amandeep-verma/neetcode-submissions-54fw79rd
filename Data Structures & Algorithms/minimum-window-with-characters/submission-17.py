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
        Sol 2 brute force - made better
        Avoiding compare entire dictionary each time
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

            # Notice if first character is not in dict1. it can not be shortest substring
            if s[i] not in myDict1:
                continue

            myDict2 = {}
            matchSet = set()

            for j in range(i, len(s)):
                
                myDict2[s[j]]= 1+ myDict2.get(s[j], 0)
                # Instead of comparing the entire dictionary each time, just compare the new element
                # and keep a count of it
                if s[j] not in matchSet and s[j] in myDict1 and myDict2[s[j]] >= myDict1[s[j]]:
                    matchSet.add(s[j])

                if len(matchSet) == len(myDict1):
                    if not ssPresent or (len(s[i:j+1]) < len(ss)):
                        ss = s[i:j+1]
                    
                    ssPresent= True
                    break
        return ss

        








        