class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        """ 
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        valid_operators_map = {"+": lambda x,y : x+y, "-": lambda x,y: x-y, "*": lambda x,y : x*y, "/": lambda x,y : int(x/y)}

        stack = []
        for token in tokens:
            if token in valid_operators_map:
                y = stack.pop()
                x = stack.pop()
                stack.append(valid_operators_map[token](x,y))
            else:
                stack.append(int(token))
        return stack.pop()