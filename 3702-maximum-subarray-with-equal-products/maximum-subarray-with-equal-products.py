class Solution:
    def maxLength(self, nums: List[int]) -> int:
        """
        Time Complexity = O(n²log M); where, M is the maximum value involved in the GCD/LCM calculations.
        Space Complexity = O(1)
        """
        n = len(nums)
        result = 0
        for i in range(n):
            g = 0
            l = 1
            product = 1
            for j in range(i,n):
                product *= nums[j]
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                if product == g*l:
                    result = max(result, j-i+1)
        return result