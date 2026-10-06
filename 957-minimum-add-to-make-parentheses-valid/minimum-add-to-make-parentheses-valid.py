class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        insertions = 0
        open_count = 0
        for ch in s:
            if ch=="(":
                open_count+=1
            else:
                if open_count==0:
                    insertions+=1
                else:
                    open_count-=1
        insertions += open_count
        return insertions