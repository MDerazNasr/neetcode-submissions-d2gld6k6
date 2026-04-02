class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        [5,4,3,2,1]
    
        '''
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]

        

        
