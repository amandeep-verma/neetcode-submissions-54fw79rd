class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sol1 - brute force
        # 
        # O(n)


        myDict = defaultdict(list)
        mySet = set()

        for item in strs:
            key = [0] *26

            for c in item:
                key[ord(c)-ord('a')] += 1

            myDict[tuple(key)].append(item)

        return list(myDict.values())


