class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        right, left = len(s)-1 ,0

        while right > left :
            if not s[right].isalnum():
                right -= 1
                continue
            if not s[left].isalnum():
                left += 1
                continue
            
            if s[right].lower() != s[left].lower():
                return False
            
            right -= 1
            left += 1
        

        return True