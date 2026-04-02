# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        counter = 0
        stack = [(root,root.val)]

        while stack:
            node, largest = stack.pop()

            if node.val >= largest:
                counter += 1
                largest = max(largest, node.val)
            
            if node.left:
                stack.append((node.left, largest))
            if node.right:
                stack.append((node.right,largest))
        return counter