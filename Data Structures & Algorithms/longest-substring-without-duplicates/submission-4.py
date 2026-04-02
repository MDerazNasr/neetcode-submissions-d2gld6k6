class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        strCount = set()
        l = 0

        for r in range(len(s)):
            while s[r] in strCount:
                strCount.remove(s[l])
                l += 1
            strCount.add(s[r])
            longest = max(longest, len(strCount))

        return longest