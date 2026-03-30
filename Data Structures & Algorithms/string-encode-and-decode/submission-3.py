class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return chr(390)
        newVal = ""
        for i,v in enumerate(strs):
            newVal = newVal + v if i == len(strs)-1 else newVal + v + chr(290)
        
        print(newVal)
        return newVal

    def decode(self, s: str) -> List[str]:
        newList = []
        if chr(390) in s:
            return newList
        strs = s.split(chr(290))
        
        for i,v in enumerate(strs):
            newList.append(v)
            
        return newList
