class Solution:
    def isValid(self, s: str) -> bool:

        """
        Sol 1: make a map of open close brackets. Add element to stack if they are opening bracket else
        pop element from stack and see if it matches to corresponding bracket from mydict

        O(n)
        """

        myMap = {'[':']', '{':'}', '(':')'}

        stack = []

        for ch in s:
            if ch not in myMap:
                if stack and myMap[stack[-1]] == ch:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
