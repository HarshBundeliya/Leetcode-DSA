# Time Complexity = O(1)
# Space Complexity = O(n)
class MinStack:

    def __init__(self):
        self.values = []
        self.min_stack = [float('inf')]

    def push(self, value: int) -> None:
        self.values.append(value)
        self.min_stack.append(min(value,self.min_stack[-1]))

    def pop(self) -> None:
        self.values.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.values[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()