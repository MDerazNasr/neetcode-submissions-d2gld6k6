class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for string in strs:
            freq = [0]*26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            if tuple(freq) in ans:
                ans[tuple(freq)].append(string)
            else:
                ans[tuple(freq)] = [string]

        return list(ans.values())


            
        

    



        