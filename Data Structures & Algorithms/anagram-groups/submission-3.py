class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Sol1 - brute force
        # 
        # O(n)
        def isAnagram(s: str, t: str) -> bool:

            if len(s) != len(t):
                return False
            
            myDict = defaultdict(int)

            for i in range(len(s)):
                myDict[s[i]] +=1
                myDict[t[i]] -=1

            for k,v in myDict.items():
                if v != 0:
                    return False

            return True

        myDict = defaultdict(list)
        mySet = set()

        for i in range(len(strs)):
            if i in mySet:
                continue

            myDict[strs[i]].append(strs[i])
            for j in range(i+1, len(strs)):

                if (isAnagram(strs[i],strs[j])):
                    myDict[strs[i]].append(strs[j])
                    mySet.add(j)

        return list(myDict.values())


