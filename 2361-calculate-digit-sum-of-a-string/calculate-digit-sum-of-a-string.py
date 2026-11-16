class Solution:
    def digitSum(self, s: str, k: int) -> str:
        """
        Time Complexity = O(nlogn) 
        Space Complexity = O(n)
        """
        def Divide_Merge(s):
            result = []
            i = 0
            current_num = 0
            for num in s:
                current_num += int(num)
                i+=1
                if i == k:
                    result.append(str(current_num))
                    current_num = 0
                    i = 0 
            if i>0:           
                result.append(str(current_num))
            return "".join(result)

        output = s
        while len(output)> k:
            output = Divide_Merge(output)

        return output
