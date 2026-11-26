class Solution:
    def canAliceWin(self, n: int) -> bool:
        """
        Time complexity = O(10) = O(1)
        Space Complexity = O(1)
        """
        Alice_win = False
        for i in range(10,0,-1):
            if n < i:
                return Alice_win
            n -= i
            Alice_win = not Alice_win