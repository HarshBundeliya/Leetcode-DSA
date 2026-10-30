import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        """
        Time Complexity: O((n*k + E*k) * log(n*k))
        Space Complexity: O(n*k + E)
        """
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # dist[node][run] = minimum cost to reach node
        # with the current consecutive character run.
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        initial_run = 1
        dist[0][initial_run] = 0

        # (cost, node, consecutive_count)
        min_heap = [(0, 0, initial_run)]

        while min_heap:
            cost, u, run = heapq.heappop(min_heap)

            if cost != dist[u][run]:
                continue

            if u == n - 1:
                return cost

            for v, weight in graph[u]:
                if labels[u] == labels[v]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[v][new_run]:
                    dist[v][new_run] = new_cost
                    heapq.heappush(
                        min_heap,
                        (new_cost, v, new_run)
                    )

        return -1