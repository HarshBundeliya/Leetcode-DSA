class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        """
        Time Complexity = O(nm); where m = r-l+1 ; worst = O(n**2)
        Space Complexity = O(1)
        """
        n = len(nums)
        result = float("inf")
        
        for k in range(l,r+1):
            left = 0
            right = k
            current_sum = sum(nums[left:right])
            if current_sum >0:
                    result = min(result,current_sum)
            while right < n:
                current_sum = current_sum + nums[right] - nums[left]
                right += 1
                left += 1
                if current_sum > 0:
                    result = min(result, current_sum)
        return -1 if result==float("inf") else result