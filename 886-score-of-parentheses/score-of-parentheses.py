class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        stack = [0]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(0)
            else:
                inner_score = stack.pop()
                if inner_score == 0:
                    score = 1
                else:
                    score = inner_score * 2
                stack[-1] += score
        
        return stack[0]
                    
