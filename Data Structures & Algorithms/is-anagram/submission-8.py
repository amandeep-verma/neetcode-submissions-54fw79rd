class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # count1 = Counter(s)
        # count2 = Counter(t)

        # return count1 == count2

        if len(s) != len(t):
            return False

        myList1 = [0] *26

        for i in range(len(s)):
            myList1[ord(s[i])-ord('a')] += 1
            myList1[ord(t[i])-ord('a')] -= 1

        for i in myList1:
            if i != 0:
                return False

        return True