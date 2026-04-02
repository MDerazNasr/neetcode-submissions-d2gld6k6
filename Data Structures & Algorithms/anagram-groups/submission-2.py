class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            freq = [0] * 26
            for c in string:
                code = ord(c) - ord('a')
                freq[code] += 1
            
            if tuple(freq) in ans:
                ans[tuple(freq)].append(string)
            else:
                ans[tuple(freq)] = [string]
        return list(ans.values())
        