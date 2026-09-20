class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Time complexity = O(n)
        # Space Complexity = O(1)
        all_product = 1
        non_zero_all_product = 1
        zero_c = 0
        for i in nums:
            if i!=0:
                non_zero_all_product = i*non_zero_all_product
            else:
                zero_c +=1
            all_product = i * all_product
            
        for i, num in enumerate(nums):
            if num!= 0:
                nums[i] = int(all_product/num)
            elif zero_c>1:
                nums[i] = 0
            else:
                nums[i] = non_zero_all_product
        return nums