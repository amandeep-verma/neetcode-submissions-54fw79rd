class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Sol1 Brute force 
        O(n*n)
        """
        
        result = []

        for i in range(len(temperatures)):
            flagWarmerDay = False
            for j in range(i+1,len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    flagWarmerDay = True
                    break
            result.append(j-i if flagWarmerDay else 0)

        return result



