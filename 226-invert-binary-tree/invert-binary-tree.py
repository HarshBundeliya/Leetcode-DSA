# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        """
        Time Complexity = O(n)
        Space Complexity = O(h); h = recursion call stack, where h is the tree height.
        """
        if not root:
            return

        self.invertTree(root.left)
        self.invertTree(root.right)

        root.left, root.right = root.right, root.left
        
        return root