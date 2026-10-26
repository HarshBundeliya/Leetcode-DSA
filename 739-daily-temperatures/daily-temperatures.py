class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Time Complexity = O(n^2)
        Space Complexity = O(1)
        """
        # n = len(temperatures)
        # res = []
        # for i in range(n):
        #     count = 0
        #     found = False
        #     for j in range(i+1,n):
        #         count+=1
        #         if temperatures[i]<temperatures[j]:
        #             res.append(count)
        #             found = True
        #             break
        #     if not found:
        #         res.append(0)     
        # return res

        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        n = len(temperatures)
        result =[0] * n
        stack = []
        for current_index, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                previous_index = stack.pop()
                result[previous_index] = current_index - previous_index
            stack.append(current_index)

        return result
