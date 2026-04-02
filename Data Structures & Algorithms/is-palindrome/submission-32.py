class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l,r = 0, len(s)-1

        while l < r:
            while l < r and not self.isLetter(s[l]):
                l += 1
            while l < r and not self.isLetter(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def isLetter(self, char):
        return (
            ord('a') <= ord(char) <= ord('z')
            or ord('A') <= ord(char) <= ord('Z')
            or ord('0') <= ord(char) <= ord('9')
        )
        