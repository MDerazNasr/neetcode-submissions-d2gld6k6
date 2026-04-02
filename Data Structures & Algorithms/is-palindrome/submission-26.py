class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        string = s.lower()

        while l<r:
            while not self.alphaNum(string[l]) and l<r:
                l += 1
            while not self.alphaNum(string[r]) and l<r:
                r -= 1

            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))

        