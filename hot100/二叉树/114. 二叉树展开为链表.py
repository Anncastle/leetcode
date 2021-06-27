# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        max_right = root
        while len(stack) > 0:
            root = stack.pop()
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

            if max_right != root:
                max_right.right = root
                max_right.left = None
                max_right = max_right.right






