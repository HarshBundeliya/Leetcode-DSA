class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        Time Complexity = O(n)
        Space Complexity = O(n)
        """
        n = len(nums)
        count = defaultdict(int)
        
        for num in nums:
            count[num] += 1
        
        buckets = [[] for _ in range(n+1)]
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for freq in range(n, 0, -1):
            for num in buckets[freq]:
                result.append(num)
                k-=1
                if k == 0:
                    return result
        return result