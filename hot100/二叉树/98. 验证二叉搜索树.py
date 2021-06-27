# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 第一种方法：递归
# import math
# class Solution:
#     def isValidBST(self, root: TreeNode) -> bool:
#         lower = -math.inf
#         upper = math.inf
#         return self.help(root, lower, upper)
#
#     def help(self, root: TreeNode, lower, upper):
#         if not root:
#             return True
#         elif root.val <= lower or root.val >= upper:
#             return False
#         else:
#             return self.help(root.left, lower, root.val) \
#                    and self.help(root.right, root.val, upper)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 第二种方法：中序遍历
import math
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        max_value = -math.inf

        while root is not None or len(stack) > 0:
            if root is not None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if root.val > max_value:
                    max_value = root.val
                else:
                    return False
                root = root.right
        return True



