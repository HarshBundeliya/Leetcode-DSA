# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """
        Time Complexity: O(n)
        Space Complexity: O(h), where h is the height of the tree.
        Worst case: O(n) for a skewed tree.
        Best case: O(log n) for a balanced tree.
        """

        def validate(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False

            return (
                validate(node.left, low, node.val) and
                validate(node.right, node.val, high)
            )

        return validate(root, float('-inf'), float('inf'))

# class Solution:
#     def isValidBST(self, root: TreeNode | None) -> bool:
#         """
#         Time Complexity = O(n)
#         Space Complexity = O(h); h = height of tree, worst = O(n)
#         """
#         if not root:
#             return True
        
#         if (root.left and root.right) and (root.left.val > root.val or root.right.val < root.val):
#             return False
        
#         left = self.isValidBST(root.left, root)
#         right = self.isValidBST(root.right, root)

#         return left and right