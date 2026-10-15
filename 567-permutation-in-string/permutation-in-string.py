class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Time Complexity = O(n1+n2)
        Space Complexity = O(26)
        """
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2:
            return False

        def utiles(d):
            for i in range(97,123):
                d[i] = 0

        s1_map = {}
        utiles(s1_map)
        for s in s1:
            s1_map[ord(s)] = s1_map.get(ord(s), 0) + 1

        current_s2_map = {}
        utiles(current_s2_map)
        for i in range(n1):
            current_s2_map[ord(s2[i])] = current_s2_map.get(ord(s2[i]), 0) + 1

        if s1_map == current_s2_map:
            return True
        
        for i, s in enumerate(s2[n1:]):
            current_s2_map[ord(s)] = current_s2_map.get(ord(s), 0) + 1
            current_s2_map[ord(s2[i])] = current_s2_map[ord(s2[i])] - 1
            if s1_map == current_s2_map:
                return True 
        return False