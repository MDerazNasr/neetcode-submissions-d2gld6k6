class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = defaultdict(int)
        tset = defaultdict(int)

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            sset[s[i]] += 1
            tset[t[i]] += 1
        return sset == tset