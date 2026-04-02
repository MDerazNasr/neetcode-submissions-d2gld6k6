# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        q = deque()
        q.append((root, root.val))
        res = 0

        while q:
            curr_len = len(q)
            for i in range(curr_len):
                node, prev = q.popleft()

                if node.val >= prev:
                    res += 1
                if node.left:
                    q.append((node.left, max(prev, node.left.val)))
                if node.right:
                    q.append((node.right, max(prev, node.right.val)))
        return res

            
        