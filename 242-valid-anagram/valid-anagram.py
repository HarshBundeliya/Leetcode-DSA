class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time Complexity = O(n)
        # Space Complexity = O(n*m)
        if len(s) != len(t):
            return False
        
        s_map = {}
        for i in s:
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1
        
        t_map = {}
        for j in t:
            if j in t_map:
                t_map[j] += 1
            else:
                t_map[j] = 1

        for k, v in s_map.items():
            if k in t_map and v ==  t_map[k]:
                pass
            else:
                return False
        return True