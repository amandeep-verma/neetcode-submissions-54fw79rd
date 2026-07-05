class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Sol1 Brute force 
        O(n*n)
        """
        
        # result = []

        # for i in range(len(temperatures)):
        #     flagWarmerDay = False
        #     for j in range(i+1,len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             flagWarmerDay = True
        #             break
        #     result.append(j-i if flagWarmerDay else 0)

        # return result

        """ Sol 2 Brute force 
        O(n*n)

        [30,38,30,36,35,40,28]

         40, 28

        1, 4, 1, 2, 1

        """

        result = [0] * len(temperatures)
        stack = []

        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                top = stack.pop()
                result[top[1]] = i - top[1]

            stack.append((val, i))

        return result



