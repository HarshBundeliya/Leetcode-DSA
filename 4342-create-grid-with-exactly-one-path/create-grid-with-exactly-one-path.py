class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        """
        Time Complexity = O(mn)
        Space Complexity = O(1)
        """
        result = ["."*n]
        for _ in range(m-1):
            result.append("#"*(n-1) + ".")
        return result