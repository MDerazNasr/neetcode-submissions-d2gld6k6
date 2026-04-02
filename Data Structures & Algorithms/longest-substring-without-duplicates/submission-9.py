class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxWindow = 0
        l = 0
        window = []
        
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.append(s[r])
            maxWindow = max(maxWindow, len(window))
        return maxWindow