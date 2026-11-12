class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """ 
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        # result = 1
        # increasing = 1
        # decreasing = 1
        # for i in range(1,len(nums)):
        #     if nums[i]>nums[i-1]:
        #         increasing += 1
        #     else:
        #         result = max(result, increasing)
        #         increasing = 1
        #     result = max(result, increasing)

        # for i in range(1,len(nums)):
        #     if nums[i]<nums[i-1]:
        #         decreasing += 1
        #     else:
        #         result = max(result, decreasing)
        #         decreasing = 1
        #     result = max(result, decreasing)

        # return result

        """ 
        Time Complexity = O(n)
        Space Complexity = O(1)
        """
        result = 1
        increasing = 1
        decreasing = 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increasing += 1
                result = max(result, decreasing)
                decreasing = 1
            elif nums[i]<nums[i-1]:
                decreasing += 1
                result = max(result, increasing)
                increasing = 1
            else:
                result = max(result, increasing)
                increasing = 1
                result = max(result, decreasing)
                decreasing = 1
            result = max(result, increasing)
            result = max(result, decreasing)
        return result