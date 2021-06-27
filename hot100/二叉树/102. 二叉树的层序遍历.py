# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        ret = [[root.val]]
        queue = [root]
        level = []
        while len(queue) > 0:
            root = queue.pop(0)
            if root.left is not None:
                queue.append(root.left)
                level.append(root.left.val)
            if root.right is not None:
                queue.append(root.right)
                level.append(root.right.val)
            if len(level) > 0 and len(queue) == len(level):
                ret.append(level)
                level = []
        return ret
