class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        first_s = s[0]
        indexes = [i for i, char in enumerate(goal) if char==first_s]
        if len(indexes)==0:
            return False
        for index in indexes:
            rotated_goal = goal[index:] + goal[:index]
            if s==rotated_goal:
                return True
        return False