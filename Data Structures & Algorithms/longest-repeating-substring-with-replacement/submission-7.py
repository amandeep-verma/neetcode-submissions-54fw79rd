class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        
        mySet = set()
        myDict = {}
        maxLength = 0

        tempStart = 0
        tempMaxRep = 0 

        for i, val in enumerate(s):

            myDict[val] = 1+ myDict.get(val, 0)

            #  find the key for which myDict value is max
            maxKey = list(myDict.keys())[0]
            for key in myDict.keys():
                if myDict[key] >= myDict[maxKey]:
                    maxKey = key
            
            valueToBeReplaced = 0
            for key in myDict.keys():
                if key != maxKey:
                    valueToBeReplaced += myDict[key]
            
            while valueToBeReplaced > k and tempStart < len(s):
                currChar = s[tempStart]

                if myDict[currChar] > 1:
                    myDict[currChar] = myDict[currChar] - 1
                else:
                    myDict.pop(currChar)

                for key in myDict.keys():
                    if myDict[key] >= myDict[maxKey]:
                        maxKey = key
            
                valueToBeReplaced = 0
                for key in myDict.keys():
                    if key != maxKey:
                        valueToBeReplaced += myDict[key]

                tempStart += 1
            
            maxLength = max(maxLength, i- tempStart +1)
        

        return maxLength