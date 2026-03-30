class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        """
        Sol 1 brute force
        compare sorted s1 with sorted subtring of s2
        O(n*n)
        """


        """
        Sol 2 Sliding window
        make a hashmap of s1 and compare it with updating hashmap of sliding window of size s1 in s2
        O(26*n)
        """

        # if len(s1) > len(s2):
        #     return False

        # myDict1 = {}
        # for char in s1:
        #     myDict1[char]= 1+ myDict1.get(char, 0)

        # l, r = 0, len(s1) 
        # myDict2 = {}
        # for i in range(len(s1)):
        #     myDict2[s2[i]]= 1+ myDict2.get(s2[i], 0)


        # while r < len(s2):

        #     if myDict1== myDict2:
        #         return True

        #     myDict2[s2[r]]= 1+ myDict2.get(s2[r], 0)

        #     if myDict2[s2[l]] > 1:
        #         myDict2[s2[l]] -= 1
        #     else:
        #         myDict2.pop(s2[l])
            
        #     r += 1
        #     l += 1
            
        
        # return myDict1== myDict2


        """
        Sol 3 Sliding window
        make a list bucket for count of s1 and s2 
        Maintaining a count of matches 
        O(26*n)


        caabb
        uieraaacbbrkr

        """

        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')

            if s1Count[index] == s2Count[index]:
                matches -= 1
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            

            index = ord(s2[l]) - ord('a')

            if s1Count[index] == s2Count[index]:
                matches -= 1
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            
            l += 1
        return matches == 26


        