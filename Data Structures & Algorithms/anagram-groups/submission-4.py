class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for string in strs:
            freq = [0] * 26
            for c in string:
                code = ord(c) - ord('a')
                freq[code] += 1
            freq = tuple(freq)
            if freq in ans:
                ans[freq].append(string)
            else:
                ans[freq] = [string]
            
        return list(ans.values())
