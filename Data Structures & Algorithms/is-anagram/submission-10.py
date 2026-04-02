class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = collections.defaultdict(int)
        tset = collections.defaultdict(int)
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sset[s[i]] += 1
            tset[t[i]] += 1

        # tsorted = dict(sorted(tset.items()))
        # ssorted = dict(sorted(sset.items()))
        return sset == tset