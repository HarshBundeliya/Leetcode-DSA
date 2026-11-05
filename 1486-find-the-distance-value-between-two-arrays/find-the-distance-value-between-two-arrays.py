class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        """
        Time Complexity = O(n**2)
        Space Complexity = O(1)
        x-d <= y <= x+d

        arr2 = [1, 4, 8, 10, 15]
        x = 8
        d = 2
        [6,10] not allowed 
        """
        m = len(arr2)
        arr2.sort()
        count = 0
        for x in arr1:
            left = 0
            right = m
            while left < right:
                mid = (left+right)//2
                if arr2[mid] < x-d:
                    left = mid+1
                else:
                    right = mid      
            if left == len(arr2) or arr2[left] > x + d:
                count += 1 
        return count