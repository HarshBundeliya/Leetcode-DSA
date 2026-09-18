class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Time Complexity = O(n)
        # Space Complexity = O(n)
        map = {}
        for i, num in enumerate(nums):
            if num in map:
                map[num].append(i)
            else:
                map[num] = [i]
        for i, num in enumerate(nums):
            sec_num = target-num
            if sec_num in map:
                sec_num_index = map[sec_num]
                if sec_num_index==[i]:
                    continue
                elif len(sec_num_index)==1:
                    return [i,sec_num_index[0]]
                else:
                    return sec_num_index