class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        Time Complexity = O(n)
        Space Complexity = O(1)

        Incrementing n-1 elements is equivalent to decrementing one element. 
        So, make every element equal to the minimum.
        
        Original problem: Increment n-1 elements until all are equal.
        Equivalent problem: Decrement one element at a time until all are equal.
        """
        
        result = 0
        minimum = min(nums)
        for num in nums:
            result += num - minimum
        return result

# {1, 3, 5, 7, 10}
# {10, 12, 14, 16, 10}  -- 9
# {16, 18, 20, 16, 16}  -- 6
# {20, 22, 20, 20 , 20}  -- 4
# 22                     -- 2