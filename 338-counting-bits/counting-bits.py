class Solution:
    def countBits(self, n: int) -> list[int]:
        """
        Time Complexity = O(32n)
        Space Complexity = O(n)
        """
        # result = []
        # for i in range(n+1):
        #     count = 0
        #     while i:
        #         i = i & (i-1)
        #         count+=1
        #     result.append(count)
        # return result

        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        
        i >> 1 means remove the last binary bit.
        i & 1 means check the last bit
        i >> 1 gives you the number with the last bit removed, 
        and i & 1 tells you whether that removed bit was 1.
        """
        result = [0] * (n+1)
        for i in range(n+1):
            result[i] = result[i >> 1] + (i & 1) # result[i//2] + (i%2)
        return result
