class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        """
        Time Complexity: O((n + q) * log(n))
        Space Complexity: O(n * log(n)), primarily for binary lifting.
        """
        from math import inf

        # Build the tree.
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def char_mask(c):
            return 1 << (ord(c) - ord('a'))

        # Iterative DFS: Euler tour, depths, parents and root-prefix masks.
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        prefix_mask = [0] * n
        timer = 0

        stack = [(0, -1, False)]

        while stack:
            u, p, exiting = stack.pop()

            if exiting:
                tout[u] = timer - 1
                continue

            parent[u] = u if p == -1 else p
            tin[u] = timer
            timer += 1

            prefix_mask[u] = (
                char_mask(s[u])
                if p == -1
                else prefix_mask[p] ^ char_mask(s[u])
            )

            stack.append((u, p, True))

            for v in reversed(graph[u]):
                if v != p:
                    depth[v] = depth[u] + 1
                    stack.append((v, u, False))

        # Binary lifting for LCA.
        LOG = n.bit_length()
        up = [parent[:]]

        for k in range(1, LOG):
            previous = up[k - 1]
            up.append([previous[previous[u]] for u in range(n)])

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            bit = 0

            while diff:
                if diff & 1:
                    u = up[bit][u]
                diff >>= 1
                bit += 1

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if up[k][u] != up[k][v]:
                    u = up[k][u]
                    v = up[k][v]

            return parent[u]

        # Fenwick tree supporting subtree range-XOR updates
        # and point queries.
        bit = [0] * (n + 2)

        def update_bit(index, delta):
            while index <= n + 1:
                bit[index] ^= delta
                index += index & -index

        def query_bit(index):
            result = 0
            while index > 0:
                result ^= bit[index]
                index -= index & -index
            return result

        def update_subtree(u, delta):
            update_bit(tin[u] + 1, delta)
            update_bit(tout[u] + 2, delta)

        def current_prefix(u):
            return prefix_mask[u] ^ query_bit(tin[u] + 1)

        chars = list(s)
        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_char = parts[2]

                delta = char_mask(chars[u]) ^ char_mask(new_char)
                update_subtree(u, delta)
                chars[u] = new_char

            else:
                u = int(parts[1])
                v = int(parts[2])

                ancestor = lca(u, v)

                path_mask = (
                    current_prefix(u)
                    ^ current_prefix(v)
                    ^ char_mask(chars[ancestor])
                )

                answer.append(path_mask.bit_count() <= 1)

        return answer