class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # Time Complexity = O(num)
        # Space Complexity = O(1)
        
        if sum > 9*num:
            return ""
        
        count_9 = 0
        for i in range(num):
            if sum - 9 >= 0:
                count_9 +=1
                sum -= 9
            else:
                if sum == 0:
                    return "9"*count_9 + "0"*(num-count_9)
                return "9"*count_9 + str(sum) + "0"*(num-count_9-1)
        
        return "9"*count_9 