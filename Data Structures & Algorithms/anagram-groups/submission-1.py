class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getAsciiCount(str1:str)-> List[int]:
            myList = [0] * 26
            for c in str1:
                myList[ord(c)-ord('a')] += 1
            return myList
        

        myDict = defaultdict(list)

        for word in strs:
            myList = getAsciiCount(word)
            myTuple = tuple(myList)

            myDict[myTuple].append(word)

        return list(myDict.values())


        # # O (n)
        # def checkAnagrams(str1:str, str2:str)-> boolean:
        #     if len(str1) != len(str2):
        #         return False

        #     myList = [0] *26

        #     for i in range(len(str1)):
        #         myList[ord(str1[i])- ord('a')] += 1
        #         myList[ord(str2[i])- ord('a')] -= 1

        #     for val in myList:
        #         if val != 0:
        #             return False

        #     return True

