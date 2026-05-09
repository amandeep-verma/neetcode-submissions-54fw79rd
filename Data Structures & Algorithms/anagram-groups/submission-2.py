class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getAsciiCount(str1:str)-> List[int]:
            myList = [0] * 26
            for c in str1:
                myList[ord(c)-ord('a')] += 1
            return myList
        
        myDict = defaultdict(list)

        # O (n * m)
        for word in strs:
            
            myList = getAsciiCount(word)
            myTuple = tuple(myList)

            myDict[myTuple].append(word)

        return list(myDict.values())