class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()

        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.isAlpha(s[l]):
                l += 1
            while l < r and not self.isAlpha(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
        
    def isAlpha(self, z):
        return (ord('a') <= ord(z) <= ord('z') or
        ord('A') <= ord(z) <= ord('Z') or
        ord('0') <= ord(z) <= ord('9'))

        