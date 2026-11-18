# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity = O(h); h = height of binary tree, Balanced BST	O(log n), Skewed BST O(n)
        Space Complexity = O(1)

        When a problem gives you a BST, 
        always look for opportunities to use its ordering property 
        instead of traversing the entire tree.
        """
        while root:
            current_val = root.val
            if p.val < current_val and q.val < current_val:
                root = root.left
            elif p.val > current_val and q.val > current_val:
                root = root.right
            else:
                return root