class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        ss = ""

        # to identify if we have a solution just make dictionary of both s and t.
        # if all keys of t have same value => in t, we have a solution
        myDict1 = {}
        myDict2 = {}
        for i in range(len(t)):
            myDict1[t[i]]= 1+ myDict1.get(t[i], 0)
            # myDict2[s[i]]= 1+ myDict2.get(s[i], 0)

        for i in range(len(s)):
            myDict2[s[i]]= 1+ myDict2.get(s[i], 0)

        for key, val in myDict1.items():
            if val > myDict2.get(key, 0):
                return ""
        
        myDict2 = {}
        for i in range(len(t)-1):
            myDict2[s[i]]= 1+ myDict2.get(s[i], 0)
        
        ss = s
        l, r = 0, len(t)


        for r in range(len(t)-1, len(s)):

            myDict2[s[r]] = myDict2.get(s[r],0)+1
            print(myDict2)
            # if s[l] not in myDict2:
            #     l += 1
            #     myDict1[s[l]] = myDict1.get(s[l]) - 1
            #     r += 1
            #     myDict1[s[r]] = myDict1.get(s[r], 0) - 1

            match = True
            for key, val in myDict1.items():
                if val > myDict2.get(key, 0):
                    match = False
                    break
            print(match)
            
            while match and l<= r:
                print(s[l:r+1])
                
                if r-l+1 < len(ss):
                    ss = s[l:r+1]
                
                if myDict2[s[l]] == 1:
                    myDict2.pop(s[l])
                else:
                    myDict2[s[l]] -= 1
                l += 1
                print(myDict1)
                for key, val in myDict1.items():
                    print(val, "", myDict2.get(key, 0))
                    if val > myDict2.get(key, 0):
                        match = False
                        break

            
        return ss 



        """
        OUZOZDYXYAAZVYXYAPPPZ

        OUZO

        XYYZ

        ZDYXY
        YXYAAZ
        ZVYXY
        YXAYPPPZ

        x:1, y:2, z: 1

        o:2, u:1, z:1


        """
        