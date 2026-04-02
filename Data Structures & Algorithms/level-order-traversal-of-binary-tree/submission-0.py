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
        
        queue = collections.deque()
        queue.append(root)
        ans = []

        while queue:
            levels = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node:
                    levels.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if levels:
                ans.append(levels)
        return ans
