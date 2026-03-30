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
            maxKey = max(myDict, key=myDict.get)
            
            valueToBeReplaced = 0
            for key in myDict.keys():
                if key != maxKey:
                    valueToBeReplaced += myDict[key]
            
            while valueToBeReplaced > k and tempStart < len(s):
                myDict[s[tempStart]] -= 1
                    

                maxKey = max(myDict, key=myDict.get)
            
                valueToBeReplaced = 0
                for key in myDict.keys():
                    if key != maxKey:
                        valueToBeReplaced += myDict[key]

                tempStart += 1
            
            maxLength = max(maxLength, i- tempStart +1)
        

        return maxLength