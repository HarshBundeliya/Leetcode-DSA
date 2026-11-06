class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        """
        Time Complexity = O(LlogL + QlogQ); Q = len(queries), L = len(logs)
        Space Complexity = O(L + Q + n)

        When queries have overlapping time intervals, 
        consider sorting them and maintaining a sliding window 
        instead of recalculating each interval from scratch.
        """
        logs.sort(key= lambda x : x[1])
        sorted_queries = sorted(enumerate(queries), key = lambda x : x[1])
        
        result = [0] * len(queries)
        server_count = {}
        
        left = 0
        right = 0
        for index, query in sorted_queries:
            start = query - x 

            # Add logs with time <= query
            while right < len(logs) and logs[right][1] <= query:
                server_id = logs[right][0]
                server_count[server_id] = server_count.get(server_id, 0) + 1
                right += 1

            # Remove logs with time < query - x
            while left < right and logs[left][1] < start:
                server_id = logs[left][0]
                server_count[server_id] -= 1
                if server_count[server_id] == 0:
                    del server_count[server_id]
                left += 1

            result[index] = n - len(server_count)
        return result