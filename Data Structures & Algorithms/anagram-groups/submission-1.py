class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for string in strs:
            freq = [0]* 26
            for c in string:
                letter = ord(c) - ord('a')
                freq[letter] += 1
            if tuple(freq) in ans:
                ans[tuple(freq)].append(string)
            else:
                ans[tuple(freq)] = [string]
            
        return list(ans.values())
        