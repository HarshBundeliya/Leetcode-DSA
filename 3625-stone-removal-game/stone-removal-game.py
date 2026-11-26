class Solution:
    def canAliceWin(self, n: int) -> bool:
        """
        Time complexity = O(10) = O(1)
        Space Complexity = O(1)
        """
        if n < 10:
            return False
        
        Alice_turn = True
        for i in range(10,0,-1):
            n -= i
            if i & 1 == 1:
                Alice_turn = False
            else:
                Alice_turn = True
            if n<0:
                return not Alice_turn