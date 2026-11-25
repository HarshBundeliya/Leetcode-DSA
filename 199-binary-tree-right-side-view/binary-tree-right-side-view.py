# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
### BFS
# class Solution:
#     def rightSideView(self, root: TreeNode | None) -> list[int]:
#         """
#         Time Complexity = O(n)
#         Space Complexity = O(n)
#         """
#         if not root:
#             return []
#         result = []
#         queue = deque([root])
#         while queue:
#             n = len(queue)
#             for i in range(n):
#                 node = queue.popleft()
#                 if i == n-1:
#                     result.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#         return result

### DFS
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []

        def dfs(node, depth):

            # 1. Base condition
            if not node:
                return

            # 2. Check if this is the first node at this depth
            if depth == len(result):
                result.append(node.val)

            # 3. Traverse right subtree first
            dfs(node.right, depth + 1)

            # 4. Traverse left subtree
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return result