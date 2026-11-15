# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(h); recursion call stack, where h is the tree height.
        Balanced tree: O(log n), Skewed tree: O(n)
        """
        if not root:
            return 0 
        left_len = self.maxDepth(root.left)
        right_len = self.maxDepth(root.right)
        return 1 + max(left_len, right_len)