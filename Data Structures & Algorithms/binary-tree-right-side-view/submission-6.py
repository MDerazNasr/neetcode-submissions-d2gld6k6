# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = [] #add right tree nodes here
        queue = deque()
        queue.append(root)
        # ans.append(root.val)
        
        while queue:
            level = None
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node:
                    level = node
                    queue.append(node.left)
                    queue.append(node.right)                
            if level:         
                ans.append(level.val)

        return ans
            
