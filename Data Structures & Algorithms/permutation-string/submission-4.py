class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        """
        Sol 1 brute force
        compare sorted s1 with sorted subtring of s2
        O(n*n)
        """

        if len(s1) > len(s2):
            return False

        myDict1 = {}
        for char in s1:
            myDict1[char]= 1+ myDict1.get(char, 0)

        l, r = 0, len(s1) 
        myDict2 = {}
        for i in range(len(s1)):
            myDict2[s2[i]]= 1+ myDict2.get(s2[i], 0)


        while r < len(s2):


            if  myDict1== myDict2:
                return True

            myDict2[s2[r]]= 1+ myDict2.get(s2[r], 0)

            if myDict2[s2[l]] > 1:
                myDict2[s2[l]] -= 1
            else:
                myDict2.pop(s2[l])
            
            r += 1
            l += 1
            
        
        return myDict1== myDict2


        