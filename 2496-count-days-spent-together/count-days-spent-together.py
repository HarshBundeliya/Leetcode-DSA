class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        """
        Time Complexity = O(12) = O(1)
        Space Complexity = O(12) = O(1)
        """
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_before_month = [0]
        for days in days_in_month:
            days_before_month.append(days_before_month[-1] + days)

        def date_to_day_of_year(date_str):
            month, day = date_str.split("-")
            return days_before_month[int(month)-1] + int(day)
        
        arriveAlice_day = date_to_day_of_year(arriveAlice)
        leaveAlice_day = date_to_day_of_year(leaveAlice)
        arriveBob_day = date_to_day_of_year(arriveBob)
        leaveBob_day = date_to_day_of_year(leaveBob)
        
        overlap_start = max(arriveAlice_day, arriveBob_day)
        overlap_end = min(leaveAlice_day, leaveBob_day)
        if overlap_start > overlap_end:
            return 0
        return overlap_end - overlap_start + 1