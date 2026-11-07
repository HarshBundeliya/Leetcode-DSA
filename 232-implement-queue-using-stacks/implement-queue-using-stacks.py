class MyQueue:
    """
    Time Complexity:
    push() = O(1)
    pop() =	Amortized O(1); Worst-case O(n)
    peek() = Amortized O(1)
    empty() = O(1)

    Space Complexity: O(n), where n is the number of elements in the queue.

    Each element is pushed into input_stack once, 
    transferred to output_stack at most once, and removed once. 
    Therefore, n elements require O(n) total work, 
    giving O(1) amortized time per operation.
    """
    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def transfer(self):
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int:
        if not self.output_stack:
            self.transfer()
        return self.output_stack.pop() 

    def peek(self) -> int:
        if not self.output_stack:
            self.transfer()
        return self.output_stack[-1]

    def empty(self) -> bool:
        return not (bool(self.output_stack) or bool(self.input_stack))


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()