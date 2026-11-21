# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.best = 0
    def height(self, root):
        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)  

        self.best = max(self.best, left + right)
        return max(left, right) + 1
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(h)
        """
        self.height(root)
        return self.best