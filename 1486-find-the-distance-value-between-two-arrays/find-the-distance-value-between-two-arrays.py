class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """
        Time Complexity = O(n**2)
        Space Complexity = O(1)
        """
        count = 0
        for i in arr1:
            consider = True
            for j in arr2:
                if abs(i-j) <= d:
                    consider = False
                    break
            if consider:
                count+=1
        return count