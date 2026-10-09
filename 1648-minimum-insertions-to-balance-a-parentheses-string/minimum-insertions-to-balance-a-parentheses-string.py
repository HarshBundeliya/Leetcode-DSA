class Solution:
    def minInsertions(self, s: str) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        balance = 0
        output = 0
        for char in s:
            if char == "(":
                if balance%2 != 0:
                    output += 1
                    balance -= 1
                balance += 2
            else:
                if balance == 0:
                    output += 1
                    balance += 1
                else:
                    balance -= 1
        output += balance
        return output