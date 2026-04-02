class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset, tset = {}, {}
        if len(s) != len(t):
            return False

        for i in s:
            if i in sset:
                sset[i] += 1
            else:
                sset[i] = 1

        for l in t:
            if l in tset:
                tset[l] += 1
            else:
                tset[l] = 1              
        
        # tsorted = dict(sorted(tset.items()))
        # ssorted = dict(sorted(sset.items()))
        return sset == tset