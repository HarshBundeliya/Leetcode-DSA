class stack:
    def __init__(self):
        self.values = []
    def push(self, x):
        self.values.append(x)
    def pop(self):
        return self.values.pop()

# Time Complexity = O(n)
# Space complexity = O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        valied_open_close = {'(':')', '[':']', '{':'}'}
        data = stack()
        for i in s:
            if i in valied_open_close:
                data.push(i)
            else:
                if len(data.values)==0 or i != valied_open_close[data.pop()]:
                    return False
        return len(data.values)==0