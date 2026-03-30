class TimeMap:

    def __init__(self):
        self.myDict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.myDict[key] = self.myDict.get(key,[])
        self.myDict[key].append([timestamp, value])

        

    def get(self, key: str, timestamp: int) -> str:
        myList = self.myDict.get(key, [])
        if len(myList) ==0 :
            return ""
        l , r =0,  len(myList) -1
        res = ""

        while l <= r:
            m = l + (r-l)//2

            if myList[m][0] <= timestamp:
                res = myList[m][1]
                l = m + 1
            else:
                r = m -1
        
        # if res == 0 and myList[res][0] > timestamp:
        #     return ""
        return res

    # 1, 2, 4, 5, 6, 7, 8 ,9 , 10