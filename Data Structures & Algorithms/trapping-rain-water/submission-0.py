class Solution:
    def trap(self, height: List[int]) -> int:

        l_wall, r_wall = 0,0 
        l_max = [0] * len(height)
        r_max = [0] * len(height)

        for i in range(len(height)):
            j = -i -1
            l_max[i] = l_wall
            r_max[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
        
        summ = 0
        for i in range(len(height)):
            pot = min(l_max[i], r_max[i])
            summ += max(0, pot-height[i])
        
        return summ