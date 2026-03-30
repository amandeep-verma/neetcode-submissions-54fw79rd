class Solution:
    def isValid(self, s: str) -> bool:

        stack =[]

        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            elif c == "]" or c == "}" or c == ")":
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if (c == "]" and popped == "[")  or (c == "}" and popped == "{") or (c == ")" and popped == "("):
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False
        
        