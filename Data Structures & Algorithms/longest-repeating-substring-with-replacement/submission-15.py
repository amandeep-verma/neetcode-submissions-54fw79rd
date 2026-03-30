class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # l, r = 0 , 0

        # maxL = 0
        # myDict = {}
        # maxFreqChar = s[0]

        # while r < len(s):

        #     myDict[s[r]] = myDict.get(s[r], 0) +1

        #     if s[r] != maxFreqChar:

        #         for eachKey in myDict.keys():
        #             if myDict[eachKey] > myDict[maxFreqChar]:
        #                 maxFreqChar = eachKey

        #         diffChar = sum(myDict.values()) - myDict[maxFreqChar]

        #         while diffChar > k:

        #             myDict[s[l]] -= 1
        #             l += 1 

        #             for eachKey in myDict.keys():
        #                 if myDict[eachKey] > myDict[maxFreqChar]:
        #                     maxFreqChar = eachKey

        #             diffChar = sum(myDict.values()) - myDict[maxFreqChar]

        #     maxL = max(maxL, r-l +1)

        #     r += 1

        # return maxL



        l, r = 0 , 0
        maxL = 0
        heap = []
        myDict = {}
        maxFreqChar = s[0]

        while r < len(s):

            myDict[s[r]] = myDict.get(s[r], 0) +1

            if s[r] != maxFreqChar:

                for eachKey in myDict.keys():
                    if myDict[eachKey] > myDict[maxFreqChar]:
                        maxFreqChar = eachKey

                diffChar = sum(myDict.values()) - max(myDict.values())

                while diffChar > k:

                    myDict[s[l]] -= 1
                    l += 1 

                    for eachKey in myDict.keys():
                        if myDict[eachKey] > myDict[maxFreqChar]:
                            maxFreqChar = eachKey

                    diffChar = sum(myDict.values()) - max(myDict.values())

            maxL = max(maxL, r-l +1)

            r += 1

        return maxL



"""
AAABABBBBBB

A: 4
B: 1



"""