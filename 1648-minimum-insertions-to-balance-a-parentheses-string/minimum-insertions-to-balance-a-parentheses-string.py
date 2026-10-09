class Solution:
    def minInsertions(self, s: str) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        needed_closings = 0
        insertions = 0
        for char in s:
            if char == "(":
                if needed_closings%2 != 0:
                    insertions += 1
                    needed_closings -= 1
                needed_closings += 2
            else:
                if needed_closings == 0:
                    insertions += 1
                    needed_closings += 1
                else:
                    needed_closings -= 1
        return insertions + needed_closings