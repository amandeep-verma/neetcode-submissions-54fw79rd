class Solution:
    def isValid(self, s: str) -> bool:

        myMap = {'[':']', '{':'}', '(':')'}
        
        stack = []
        for i in range(len(s)):
            print(s[i])
            if s[i] not in myMap:
                if not stack or myMap[stack[-1]] != s[i]:
                    return False
                
                stack.pop()
            
            else:
                stack.append(s[i])

        return stack == []
