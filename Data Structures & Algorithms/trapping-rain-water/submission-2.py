class Solution:
    def trap(self, height: List[int]) -> int:
        r_wall = 0
        l_wall = 0
        r_max = [0] * len(height)
        l_max = [0] * len(height)

        for i in range(len(height)):
            j = -i -1
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            l_max[i] = l_wall
            r_max[j] = r_wall
        
        ans = 0
        for i in range(len(height)):
            ans += min(l_max[i], r_max[i]) - height[i]

        return ans
