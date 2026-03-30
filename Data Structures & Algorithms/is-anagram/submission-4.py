class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        """ Sol 1 - sort them and check if both are same 
        O(n(logn)) """
        # return sorted(s) == sorted(t)

        """ Sol 2 - use an array of size 26, for each character's ASCII value from s increment the index 
        and for t decrement the index. Later go through the array and check if all elment in array are 0
        O(n) """
        # if len(s) != len(t):
        #     return False

        # myArr = [0] * 26

        # for i in range(len(s)):
        #     myArr[ord(s[i])- 97] += 1
        #     myArr[ord(t[i])- 97] -= 1

        # for o in myArr:
        #     if o != 0:
        #         return False
        
        # return True

        """ Sol 3 - use a hashSet, for each character's ASCII value from s increment the index 
        and for t decrement the index. Later go through the array and check if all elment in array are 0
        O(n) """
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i] , 0) + 1
            dict2[t[i]] = dict2.get(t[i], 0) + 1

        print(dict1)
        return dict1 == dict2




        