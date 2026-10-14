class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Time complexity = O(nklog(k)) ; where n = len(strs) , k = maximum length of a string
        # Space Complexity = O(nk) ; where n = len(strs) , k = maximum length of a string
        group_map = {}
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in group_map:
                group_map[sorted_s] = []
            
            group_map[sorted_s].append(s)
        
        return list(group_map.values())