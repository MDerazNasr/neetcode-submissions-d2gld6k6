# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = [True]
        height = [0]

        def dfs(root):
            if not root:
                return True
            
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                balanced[0] = False

            return 1 + max(left,right)
        
        dfs(root)
        return balanced[0]