# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)

        level_size = len(queue) ensures that you process only 
        the nodes belonging to the current level, 
        even while adding children for the next level.
        """
        if not root:
            return []
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            level = []
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right) 
            result.append(level)
        return result