class Solution:
    def reverse(self, x: int) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        if x < 0:
            s = str(x)[1:]
        else:
            s = str(x)
        l = 0
        r = len(s)-1
        new_s = ""
        for i in range(-1,-(len(s)+1),-1):
            new_s += s[i]
        if x<0:
            res = -int(new_s)
        else:
            res = int(new_s)
        if res < (-(2)**31) or res > ((2)**31)-1:
            return 0
        else:
            return res 