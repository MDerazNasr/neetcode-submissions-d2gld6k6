# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        ans = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue) #updated every iteration
            for i in range(n):
                node = queue.popleft() #pop from the left, first in first out

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                ans.append(level)
        return ans
