class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
       
        sset = defaultdict(int)
        tset = defaultdict(int)
        for c in range(len(s)):
            sset[s[c]] += 1
            tset[t[c]] += 1
        
        return tset == sset