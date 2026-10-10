class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        # Time Complexity = O(n + M) ; where M = max(diff) <= 10^5
        # Space Complexity = O(n + M) ; where M = max(diff) <= 10^5

        n = len(nums1)
        k = k1 + k2
        diff = [abs(nums1[i]-nums2[i]) for i in range(n)]
        if sum(diff) <= k:
            return 0
        max_diff = max(diff)
        freq = [0] * (max_diff + 1)
        for d in diff:
            freq[d] += 1

        for level in range(max_diff, 0, -1):
            count = freq[level]
            if count < 1:
                continue

            if k >= count:
                freq[level] = 0
                freq[level-1] += count
                k -= count
            else:
                freq[level] -= k
                freq[level-1] += k
                k = 0 
                break

        result = 0
        for level in range(len(freq)):
            result += level*level*freq[level]
        return result