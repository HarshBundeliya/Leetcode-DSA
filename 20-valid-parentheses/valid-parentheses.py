class stack:
    def __init__(self):
        self.values = []
    def push(self, x):
        self.values = [x] + self.values
    def pop(self):
        return self.values.pop(0)

# Time Complexity = O(n)
# Space complexity = O(1)
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
        if len(data.values)>0:
            return False
        return True