class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        strCount = set()
        l, res = 0,0

        for r in range(len(s)):
            while s[r] in strCount:
                strCount.remove(s[l])
                l += 1
            strCount.add(s[r])
            res = max(res, r-l+1)
        return res        