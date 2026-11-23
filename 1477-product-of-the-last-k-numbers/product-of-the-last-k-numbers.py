class ProductOfNumbers:
    """
    Time Complexity:
    add: O(1)
    getProduct: O(1)

    Space Complexity = O(n)
    """
    def __init__(self):
        self.prefix = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = [1]
        else:
            self.prefix.append(self.prefix[-1]*num)
        
    def getProduct(self, k: int) -> int:
        n = len(self.prefix)
        if n-1-k < 0:
            return 0
        return self.prefix[n-1]//self.prefix[n-1-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)