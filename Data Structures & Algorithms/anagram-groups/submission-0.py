class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """ Sol 1 - bad - takes sorting and a for loop """
        # result = []
        # myDict = {}

        # for i,v in enumerate(strs):
        #     temp = ''.join(sorted(v))
        #     if temp not in myDict:
        #         myDict[temp] = []
        #     myDict[temp].append(v)

        # for val in myDict.values():
        #     result.append(val)

        # return result

        """ Sol 2 - Good - use dictionary and a for loop """

        myDict = defaultdict(list)

        for item in strs:
            # makes an array of size 26
            charCount = [0] *26

            for i in item:
                charCount[ord(i) - ord('a')] += 1
            
            #  since we need to store it as key in dictionary, it needs to be immutable
            charCount = tuple(charCount)

            # No need to check if charCount is present in dictionary because of defaultdict 
            myDict[charCount].append(item)
        
        return list(myDict.values())

        


