from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        """
        When arranging elements to maximize concatenation, 
        compare a + b against b + a, not a against b
        
        Normal sorting compares individual strings, 
        whereas our custom comparator compares the 
        concatenated results of two possible arrangements.
        
        For nums = [30, 3]:

        Normal reverse lexicographical sorting:
        - "30" comes before "3" because "30" > "3" lexicographically.
        - Result: "303".

        Custom comparator:
        - "30" + "3" = "303"
        - "3" + "30" = "330"
        - Since "330" > "303", 3 must come before 30.
        Result: "330".

        Time Complexity = O(nlogn * k)
        Space Complexity = O(n * k) ; where k: maximum number of digits in an element.
        for the converted strings and sorting overhead, excluding the output string
        """
        nums = [str(num) for num in nums]
        def compare(a, b):
            if a+b > b+a:
                return -1
            elif a+b < b+a:
                return 1
            else:
                return 0
        nums.sort(key=cmp_to_key(compare))
        if nums[0] == "0":
            return "0"
        return "".join(nums)