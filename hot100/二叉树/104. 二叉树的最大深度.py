# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        self.index_dict = {ele: idx for idx, ele in enumerate(inorder)}
        n = len(preorder)
        root = self.buildSubtree(preorder, inorder, 0, n - 1, 0, n - 1)
        return root

    def buildSubtree(self, preorder, inorder, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return None

        root = TreeNode(val=preorder[pre_left])
        in_root = self.index_dict[preorder[pre_left]]
        left_size = in_root - in_left
        root.left = self.buildSubtree(preorder, inorder, pre_left + 1, pre_left + left_size, in_left, in_root - 1)
        root.right = self.buildSubtree(preorder, inorder, pre_left + left_size + 1, pre_right, in_root + 1, in_right)
        return root

solution = Solution()
print(solution.buildTree([1,2,3], [3,2,1]))


