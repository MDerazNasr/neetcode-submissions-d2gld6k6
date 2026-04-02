class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = set()
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in res:
                res.remove(s[l])
                l += 1
            res.add(s[r])
            longest = max(longest, len(res))
        return longest
            
        