class Solution:

    def isAlphaNumeric(self, c: chr) -> bool:
            return True if (c >= 'A' and c<= 'Z') or (c >='a' and c<= 'z') or (c >='0' and c<= '9') else False

    def convertToLower(self, c:chr) -> chr:
        return chr(ord(c)+ 32) if c >='A' and c<= 'Z' else c

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            if not self.isAlphaNumeric(s[left]):
                left += 1
                continue
            if not self.isAlphaNumeric(s[right]):
                right -= 1
                continue
                
            if self.convertToLower(s[left]) != self.convertToLower(s[right]):
                return False
            left += 1
            right -= 1
                
            
        return True
        