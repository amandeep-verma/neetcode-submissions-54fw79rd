class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """ Sol1 Brute force 
        O(n*n)
        """



        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            if not stack or stack[-1][0] >= temperatures[i]:
                stack.append((temperatures[i],i))
            else:
                while stack and stack[-1][0] < temperatures[i]:
                    val, pos = stack.pop()
                    result[pos] = i - pos
                stack.append((temperatures[i],i))

        return result



   

        """ Sol 2 Brute force 
        O(n*n)

        [30,38,30,36,35,40,28]

         40, 28

        1, 4, 1, 2, 1

        """

        # result = [0] * len(temperatures)
        # stack = []

        # for i, val in enumerate(temperatures):
        #     while stack and stack[-1][0] < val:
        #         top = stack.pop()
        #         result[top[1]] = i - top[1]

        #     stack.append((val, i))

        # return result



