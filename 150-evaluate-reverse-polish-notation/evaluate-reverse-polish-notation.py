class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """ 
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        def divide(x, y):
            q = abs(x)//abs(y)
            if (x<0 and y<0) or (x>0 and y>0):
                return q
            return -q
        valid_operators_map = {"+": lambda x,y : x+y, "-": lambda x,y: x-y, "*": lambda x,y : x*y, "/": divide} #lambda x,y : int(x/y)}

        stack = []
        for token in tokens:
            if token in valid_operators_map:
                y = stack.pop()
                x = stack.pop()
                stack.append(valid_operators_map[token](x,y))
            else:
                stack.append(int(token))
        return stack.pop()