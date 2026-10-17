class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        """
        Time Complexity = O(nlog(n))
        Space Complexity = O(n)
        """
        target = sorted( nums, key = lambda x : (sum(int(d) for d in str(abs(x))), x) )
        
        index_map = {}
        for i, num in enumerate(target):
            index_map[num] = i
        for i in range(len(nums)):
            nums[i] = index_map[nums[i]]
        
        answer = 0
        visited = set()
        for i in range(len(nums)):
            if i in visited:
                continue 
            cycle_length = 0
            current_index = i
            while current_index not in visited:
                visited.add(current_index)
                current_index = nums[current_index]
                cycle_length += 1
            answer += max(0, cycle_length - 1)
        return answer