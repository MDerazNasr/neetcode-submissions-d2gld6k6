class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}

        for word in strs:
            freq = [0] * 26
            for letter in word:
                code = ord(letter) - ord('a')
                freq[code] += 1
            
            # hashing issue
            freq = tuple(freq)
            if freq in ans:
                ans[freq].append(word)
            else:
                ans[freq] = [word]
        return list(ans.values())