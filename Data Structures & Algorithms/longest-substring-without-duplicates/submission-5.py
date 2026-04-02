class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest, l = 0,0
        string = set()

        for r in range(len(s)):
            while s[r] in string:
                string.remove(s[l])
                l += 1
            string.add(s[r])
            longest = max(longest, len(string))
        return longest