class Solution:
    def reverse(self, x: int) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(1)
        sign = -1 if x<0 else 1
        x = abs(x)
        res = 0
        while x!=0:
            digit = x % 10
            x = x//10
            res = res * 10 + digit
        res = sign * res
        if res < -(2**31) or res > (2**31)-1:
            return 0
        return res

# res = 0
# x = 12345
# digit = x%10 = 5
# x = x//10 = 1234
# res = res*10 + digit = 5
# x = 1234
# digit = x%10 = 4
# x = x//10 = 123
# res = res*10 + digit = 54