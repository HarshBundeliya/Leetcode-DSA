class Solution:
    def checkValidString(self, s: str) -> bool:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        
        min_open = 0
        max_open = 0

        for ch in s:
            if ch == '(':
                min_open += 1
                max_open += 1

            elif ch == ')':
                min_open -= 1
                max_open -= 1

            else: 
                min_open -= 1
                max_open += 1
            
            if max_open < 0:
                return False
            
            min_open = max(0, min_open)
        
        return min_open == 0