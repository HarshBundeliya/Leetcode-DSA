class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        Time complexity = O(32) = O(1)
        Space Complexity = O(1)
        - ^ → sum without carry.
        - & followed by << 1 → calculate and shift the carry.
        - Repeat until the carry becomes zero.
        """ 
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        while b & MASK:
            carry = (a&b) << 1
            a = (a^b) & MASK
            b = carry & MASK
        return a if a <= MAX_INT else ~(a^MASK)
            
        """
        110 (6)
        011 (3)
       1001 (9)
        
        a     b
       101   100  
       001  1000  
      1001  0000 
       """