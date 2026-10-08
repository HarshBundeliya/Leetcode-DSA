class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        balance = 0
        result = []
        start = 0
        for i, char in enumerate(s):
            if char == "(":
                balance += 1
            else:
                balance -=1
                if balance == 0:
                    result.append(s[start+1:i])
                    start = i+1
        return ''.join(result)