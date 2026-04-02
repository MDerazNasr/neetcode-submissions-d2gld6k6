class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for i in strs:
            freq = [0] * 26
            for string in i:
                code = ord(string) - ord('a')
                freq[code] += 1
            freq = tuple(freq)
            if freq in ans:
                ans[freq].append(i)
            else:
                ans[freq] = [i]
        return list(ans.values())