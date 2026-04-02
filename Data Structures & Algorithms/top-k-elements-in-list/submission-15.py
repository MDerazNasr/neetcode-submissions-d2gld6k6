class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict()
        freq = defaultdict(list)

        #count elem occurences in num
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        #add freq of each element to freq
        for num, cnt in count.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res