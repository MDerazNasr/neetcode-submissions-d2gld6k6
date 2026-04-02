class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False

        cT, cS = {}, {}

        for i in range(len(s)):
            cT[t[i]] = 1 + cT.get(t[i], 0)
            cS[s[i]] = 1 + cS.get(s[i], 0)

        for c in cT:
            if cT[c] != cS.get(c,0):
                return False
        return True
