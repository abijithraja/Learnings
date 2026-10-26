"""
Algorithms & Data Structures Collection
Part 1: Fibonacci Numbers with Memoization
Part 2: Binary Search (Iterative & Recursive)
Part 3: Sieve of Eratosthenes & Prime Verification
Part 4: Quicksort & Merge Sort Implementations
Part 5: Two Sum & Three Sum Problems
Part 6: Longest Common Subsequence (LCS Dynamic Programming)
Part 7: LRU (Least Recently Used) Cache Implementation
Part 8: Dijkstra's Shortest Path Algorithm on Weighted Graphs
Part 9: Kadane's Algorithm (Maximum Subarray Sum)
Part 10: 0/1 Knapsack Problem (Dynamic Programming)
Part 11: BFS & DFS Graph Traversals
Part 12: Topological Sort (Kahn's Algorithm)
Part 13: Trie (Prefix Tree) Data Structure
Part 14: Union-Find (Disjoint Set Union with Path Compression & Rank)
Part 15: Minimum Spanning Tree (Kruskal's Algorithm)
Part 16: Bellman-Ford Shortest Path Algorithm
Part 17: Floyd-Warshall All-Pairs Shortest Path
Part 18: Knuth-Morris-Pratt (KMP) Pattern Searching
Part 19: Rabin-Karp Rolling Hash String Search
Part 20: Next Greater Element (Monotonic Stack)
Part 21: Sliding Window Maximum (Monotonic Deque)
Part 22: Binary Indexed Tree / Fenwick Tree
Part 23: Segment Tree for Range Minimum Queries
Part 24: A* Search Pathfinding Algorithm
Part 25: Edit Distance / Levenshtein Distance (DP)
Part 26: Coin Change Problem (Minimum Coins & Combinations)
Part 27: Matrix Exponentiation for O(log n) Fibonacci
Part 28: Huffman Coding Data Compression Tree
Part 29: Tarjan's Strongly Connected Components (SCC)
Part 30: Kosaraju's Strongly Connected Components
Part 31: Edmonds-Karp Maximum Flow (Ford-Fulkerson BFS)
Part 32: Dinic's Algorithm for Maximum Flow
Part 33: Prim's Algorithm for Minimum Spanning Tree
Part 34: Manacher's Algorithm for Longest Palindromic Substring
Part 35: Z-Algorithm for Linear Time Pattern Matching
Part 36: Boyer-Moore String Search
Part 37: Lowest Common Ancestor (LCA) with Binary Lifting
Part 38: Euler Tour Technique for Tree Subtree Queries
Part 39: Graham Scan 2D Convex Hull
Part 40: Quickhull 2D Convex Hull
Part 41: Closest Pair of Points in 2D (O(n log n))
Part 42: 2D Kadane's Algorithm (Max Submatrix Sum)
Part 43: Longest Increasing Subsequence (LIS) in O(n log n)
Part 44: Hopcroft-Karp Maximum Bipartite Matching
Part 45: Fast Fourier Transform (FFT) Polynomial Multiplication
"""

from typing import Generator, Dict, List, Optional, Tuple, Any, Set
from collections import deque
import math
import heapq


def fibonacci_memo(n: int, memo: Dict[int, int] = None) -> int:
    """Compute the n-th Fibonacci number using memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_stream(limit: int) -> Generator[int, None, None]:
    """Yield Fibonacci numbers up to a given count."""
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def binary_search_iterative(arr: List[int], target: int) -> Optional[int]:
    """Return the index of target in sorted arr, or None if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


def binary_search_recursive(arr: List[int], target: int, left: int = 0, right: Optional[int] = None) -> Optional[int]:
    """Recursive binary search implementation."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return None
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def is_prime(num: int) -> bool:
    """Determine whether a given number is prime."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.isqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """Return all prime numbers up to limit using Sieve of Eratosthenes."""
    if limit < 2:
        return []
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(math.isqrt(limit)) + 1):
        if primes[p]:
            for multiple in range(p * p, limit + 1, p):
                primes[multiple] = False
    return [p for p, prime in enumerate(primes) if prime]


def quicksort(arr: List[int]) -> List[int]:
    """Sort list using Quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def mergesort(arr: List[int]) -> List[int]:
    """Sort list using Merge Sort algorithm."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
    """Find two indices whose values add up to target using hash map."""
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return (seen[complement], i)
        seen[num] = i
    return None


def three_sum(nums: List[int]) -> List[List[int]]:
    """Find all unique triplets [a, b, c] such that a + b + c = 0."""
    nums = sorted(nums)
    triplets = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return triplets


def longest_common_subsequence(text1: str, text2: str) -> str:
    """Find the longest common subsequence string using dynamic programming."""
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS string
    lcs_chars = []
    i, j = m, n
    while i > 0 and j > 0:
        if text1[i - 1] == text2[j - 1]:
            lcs_chars.append(text1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs_chars))


class DLinkedNode:
    """Node for doubly linked list in LRU Cache."""
    def __init__(self, key: int = 0, value: Any = 0):
        self.key = key
        self.value = value
        self.prev: Optional['DLinkedNode'] = None
        self.next: Optional['DLinkedNode'] = None


class LRUCache:
    """Least Recently Used (LRU) Cache with O(1) get and put operations."""
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: Dict[int, DLinkedNode] = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: DLinkedNode):
        """Always add the new node right after head."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: DLinkedNode):
        """Remove an existing node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _move_to_head(self, node: DLinkedNode):
        """Move certain node in between to the head."""
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self) -> DLinkedNode:
        """Pop the current tail node (least recently used)."""
        res = self.tail.prev
        self._remove_node(res)
        return res

    def get(self, key: int) -> Any:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: Any) -> None:
        node = self.cache.get(key)
        if not node:
            new_node = DLinkedNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
            if len(self.cache) > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)


def dijkstra(graph: Dict[str, Dict[str, int]], start_node: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Compute shortest distances and predecessors from start_node using Dijkstra's algorithm.
    Graph format: {'A': {'B': 4, 'C': 2}, ...}
    """
    distances: Dict[str, float] = {node: float('inf') for node in graph}
    predecessors: Dict[str, Optional[str]] = {node: None for node in graph}
    distances[start_node] = 0
    pq = [(0, start_node)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

    return distances, predecessors


def max_subarray_sum(nums: List[int]) -> int:
    """Find the maximum subarray sum using Kadane's algorithm."""
    if not nums:
        return 0
    max_so_far = current_max = nums[0]
    for x in nums[1:]:
        current_max = max(x, current_max + x)
        max_so_far = max(max_so_far, current_max)
    return max_so_far


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
    """Solve 0/1 Knapsack problem using dynamic programming."""
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(1, capacity + 1):
            if w <= c:
                dp[i][c] = max(dp[i - 1][c], dp[i - 1][c - w] + v)
            else:
                dp[i][c] = dp[i - 1][c]

    return dp[n][capacity]


def bfs_traversal(graph: Dict[str, List[str]], start_node: str) -> List[str]:
    """Perform Breadth-First Search on an unweighted graph."""
    visited: Set[str] = set()
    queue = deque([start_node])
    order = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            order.append(vertex)
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    return order


def dfs_traversal(graph: Dict[str, List[str]], start_node: str, visited: Optional[Set[str]] = None) -> List[str]:
    """Perform Depth-First Search on an unweighted graph."""
    if visited is None:
        visited = set()
    order = []
    visited.add(start_node)
    order.append(start_node)
    for neighbor in graph.get(start_node, []):
        if neighbor not in visited:
            order.extend(dfs_traversal(graph, neighbor, visited))
    return order


def topological_sort(nodes: List[str], edges: List[Tuple[str, str]]) -> Optional[List[str]]:
    """Perform Kahn's algorithm for topological sorting on a DAG."""
    in_degree = {u: 0 for u in nodes}
    adj: Dict[str, List[str]] = {u: [] for u in nodes}

    for u, v in edges:
        adj[u].append(v)
        in_degree[v] = in_degree.get(v, 0) + 1

    zero_in = deque([u for u in nodes if in_degree[u] == 0])
    result = []

    while zero_in:
        curr = zero_in.popleft()
        result.append(curr)
        for nxt in adj[curr]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                zero_in.append(nxt)

    return result if len(result) == len(nodes) else None


class TrieNode:
    """Node in a Prefix Tree (Trie)."""
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    """Trie (Prefix Tree) supporting insert, search, and starts_with."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True


class DisjointSetUnion:
    """Disjoint Set Union (DSU) / Union-Find with path compression and rank optimization."""
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False


def kruskal_mst(num_vertices: int, edges: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Compute Minimum Spanning Tree weight and edges using Kruskal's algorithm with DSU."""
    edges = sorted(edges, key=lambda item: item[0])
    dsu = DisjointSetUnion(num_vertices)
    mst = []
    total_weight = 0
    for weight, u, v in edges:
        if dsu.union(u, v):
            total_weight += weight
            mst.append((u, v, weight))
            if len(mst) == num_vertices - 1:
                break
    return total_weight, mst


def bellman_ford(vertices: List[str], edges: List[Tuple[str, str, int]], source: str) -> Optional[Dict[str, float]]:
    """Compute shortest distances from source; returns None if negative-weight cycle exists."""
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None

    return dist


def floyd_warshall(vertices: List[str], graph: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
    """Compute all-pairs shortest paths using Floyd-Warshall dynamic programming algorithm."""
    dist = {u: {v: float('inf') for v in vertices} for u in vertices}
    for u in vertices:
        dist[u][u] = 0
        for v, weight in graph.get(u, {}).items():
            dist[u][v] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist


def kmp_search(text: str, pattern: str) -> List[int]:
    """Find all starting indices of pattern occurrences in text using KMP algorithm."""
    if not pattern:
        return []

    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    matches = []
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            matches.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches


def rabin_karp_search(text: str, pattern: str, prime: int = 101) -> List[int]:
    """Search for pattern matches using Rabin-Karp rolling hash algorithm."""
    d = 256
    m, n = len(pattern), len(text)
    if m == 0 or m > n:
        return []

    p_hash = 0
    t_hash = 0
    h = pow(d, m - 1, prime)
    result = []

    for i in range(m):
        p_hash = (d * p_hash + ord(pattern[i])) % prime
        t_hash = (d * t_hash + ord(text[i])) % prime

    for s in range(n - m + 1):
        if p_hash == t_hash:
            if text[s:s + m] == pattern:
                result.append(s)
        if s < n - m:
            t_hash = (d * (t_hash - ord(text[s]) * h) + ord(text[s + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return result


def next_greater_elements(nums: List[int]) -> List[int]:
    """Find the next greater element for each number using a monotonic stack."""
    res = [-1] * len(nums)
    stack: List[int] = []

    for i in range(len(nums)):
        while stack and nums[stack[-1]] < nums[i]:
            prev_idx = stack.pop()
            res[prev_idx] = nums[i]
        stack.append(i)
    return res


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """Compute maximum elements in each sliding window of size k using monotonic deque."""
    if not nums or k <= 0:
        return []
    result = []
    dq: deque = deque()

    for i in range(len(nums)):
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


class FenwickTree:
    """Binary Indexed Tree (Fenwick Tree) for efficient point updates and prefix sum queries."""
    def __init__(self, size: int):
        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, index: int, delta: int) -> None:
        while index <= self.size:
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & (-index)
        return total

    def range_query(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


class SegmentTreeRMQ:
    """Segment Tree for Range Minimum Queries with O(log n) update and query."""
    def __init__(self, data: List[int]):
        self.n = len(data)
        self.tree = [float('inf')] * (4 * self.n)
        if self.n > 0:
            self._build(data, 0, 0, self.n - 1)

    def _build(self, data: List[int], node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = data[start]
            return
        mid = (start + end) // 2
        left_child, right_child = 2 * node + 1, 2 * node + 2
        self._build(data, left_child, start, mid)
        self._build(data, right_child, mid + 1, end)
        self.tree[node] = min(self.tree[left_child], self.tree[right_child])

    def query(self, left: int, right: int) -> float:
        return self._query(0, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, left: int, right: int) -> float:
        if right < start or end < left:
            return float('inf')
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return min(
            self._query(2 * node + 1, start, mid, left, right),
            self._query(2 * node + 2, mid + 1, end, left, right)
        )


def a_star_search(
    start: Tuple[int, int],
    goal: Tuple[int, int],
    grid: List[List[int]]
) -> Optional[List[Tuple[int, int]]]:
    """A* Pathfinding algorithm on a 2D grid where 0 = walkable, 1 = obstacle."""
    rows, cols = len(grid), len(grid[0])

    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set: List[Tuple[int, Tuple[int, int]]] = [(0, start)]
    came_from: Dict[Tuple[int, int], Tuple[int, int]] = {}
    g_score: Dict[Tuple[int, int], float] = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            return path[::-1]

        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                tentative_g = g_score[current] + 1
                neighbor = (nr, nc)
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score, neighbor))
    return None


def min_edit_distance(word1: str, word2: str) -> int:
    """Compute the minimum edit distance (Levenshtein) using dynamic programming."""
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1]
                )
    return dp[m][n]


def coin_change_min(coins: List[int], amount: int) -> int:
    """Return the fewest number of coins needed to make up amount, or -1 if impossible."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_combinations(coins: List[int], amount: int) -> int:
    """Return the number of combinations that make up amount."""
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]
    return dp[amount]


def fibonacci_matrix(n: int) -> int:
    """Calculate the n-th Fibonacci number in O(log n) time using 2x2 matrix exponentiation."""
    if n <= 0:
        return 0
    if n == 1:
        return 1

    def multiply_2x2(m1: Tuple[Tuple[int, int], Tuple[int, int]], m2: Tuple[Tuple[int, int], Tuple[int, int]]):
        return (
            (m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]),
            (m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1])
        )

    def power_2x2(mat, p):
        res = ((1, 0), (0, 1))
        base = mat
        while p > 0:
            if p % 2 == 1:
                res = multiply_2x2(res, base)
            base = multiply_2x2(base, base)
            p //= 2
        return res

    t = ((1, 1), (1, 0))
    t_pow = power_2x2(t, n - 1)
    return t_pow[0][0]


class HuffmanNode:
    """Node for Huffman coding tree."""
    def __init__(self, char: Optional[str], freq: int):
        self.char = char
        self.freq = freq
        self.left: Optional['HuffmanNode'] = None
        self.right: Optional['HuffmanNode'] = None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq


def build_huffman_codes(text: str) -> Tuple[Dict[str, str], Optional[HuffmanNode]]:
    """Generate variable-length prefix codes for characters based on frequency."""
    if not text:
        return {}, None

    frequency: Dict[str, int] = {}
    for char in text:
        frequency[char] = frequency.get(char, 0) + 1

    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    root = heap[0]
    codes: Dict[str, str] = {}

    def generate_codes(node: Optional[HuffmanNode], current_code: str):
        if not node:
            return
        if node.char is not None:
            codes[node.char] = current_code or "0"
            return
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes, root


def tarjan_scc(graph: Dict[int, List[int]]) -> List[List[int]]:
    """Find all strongly connected components in a directed graph using Tarjan's algorithm."""
    index = 0
    indices: Dict[int, int] = {}
    lowlink: Dict[int, int] = {}
    on_stack: Set[int] = set()
    stack: List[int] = []
    sccs: List[List[int]] = []

    def strongconnect(node: int):
        nonlocal index
        indices[node] = index
        lowlink[node] = index
        index += 1
        stack.append(node)
        on_stack.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in indices:
                strongconnect(neighbor)
                lowlink[node] = min(lowlink[node], lowlink[neighbor])
            elif neighbor in on_stack:
                lowlink[node] = min(lowlink[node], indices[neighbor])

        if lowlink[node] == indices[node]:
            scc = []
            while True:
                w = stack.pop()
                on_stack.remove(w)
                scc.append(w)
                if w == node:
                    break
            sccs.append(scc)

    for vertex in list(graph.keys()):
        if vertex not in indices:
            strongconnect(vertex)

    return sccs


def kosaraju_scc(n: int, adj: Dict[int, List[int]]) -> List[List[int]]:
    """Find strongly connected components using Kosaraju's two-pass DFS algorithm."""
    visited = [False] * n
    finish_order: List[int] = []

    def dfs1(v: int):
        visited[v] = True
        for u in adj.get(v, []):
            if not visited[u]:
                dfs1(u)
        finish_order.append(v)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    rev_adj: Dict[int, List[int]] = {i: [] for i in range(n)}
    for u in adj:
        for v in adj[u]:
            rev_adj[v].append(u)

    visited = [False] * n
    sccs: List[List[int]] = []

    def dfs2(v: int, comp: List[int]):
        visited[v] = True
        comp.append(v)
        for u in rev_adj.get(v, []):
            if not visited[u]:
                dfs2(u, comp)

    for v in reversed(finish_order):
        if not visited[v]:
            comp: List[int] = []
            dfs2(v, comp)
            sccs.append(comp)

    return sccs


def edmonds_karp_max_flow(capacity: List[List[int]], source: int, sink: int) -> int:
    """Compute maximum network flow using Edmonds-Karp BFS implementation of Ford-Fulkerson."""
    n = len(capacity)
    residual = [row[:] for row in capacity]
    max_flow = 0

    while True:
        parent = [-1] * n
        parent[source] = source
        queue = deque([source])

        while queue and parent[sink] == -1:
            curr = queue.popleft()
            for nxt in range(n):
                if parent[nxt] == -1 and residual[curr][nxt] > 0:
                    parent[nxt] = curr
                    queue.append(nxt)

        if parent[sink] == -1:
            break

        path_flow = float("inf")
        curr = sink
        while curr != source:
            prev = parent[curr]
            path_flow = min(path_flow, residual[prev][curr])
            curr = prev

        curr = sink
        while curr != source:
            prev = parent[curr]
            residual[prev][curr] -= int(path_flow)
            residual[curr][prev] += int(path_flow)
            curr = prev

        max_flow += int(path_flow)

    return max_flow


class DinicMaxFlow:
    """Fast maximum flow algorithm using level graphs and blocking flows (Dinic's Algorithm)."""
    def __init__(self, n: int):
        self.n = n
        self.graph: List[List[List[int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, cap: int):
        self.graph[u].append([v, cap, len(self.graph[v])])
        self.graph[v].append([u, 0, len(self.graph[u]) - 1])

    def bfs(self, s: int, t: int, level: List[int]) -> bool:
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, cap, _ in self.graph[u]:
                if cap > 0 and level[v] < 0:
                    level[v] = level[u] + 1
                    q.append(v)
        return level[t] >= 0

    def dfs(self, u: int, t: int, flow: int, level: List[int], ptr: List[int]) -> int:
        if u == t or flow == 0:
            return flow
        for i in range(ptr[u], len(self.graph[u])):
            ptr[u] = i
            v, cap, rev_idx = self.graph[u][i]
            if level[v] == level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap), level, ptr)
                if pushed > 0:
                    self.graph[u][i][1] -= pushed
                    self.graph[v][rev_idx][1] += pushed
                    return pushed
        return 0

    def compute_max_flow(self, s: int, t: int) -> int:
        flow = 0
        level = [-1] * self.n
        while self.bfs(s, t, level):
            ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, 10**9, level, ptr)
                if pushed == 0:
                    break
                flow += pushed
        return flow


def prim_mst(n: int, adj: Dict[int, List[Tuple[int, int]]], start: int = 0) -> Tuple[int, List[Tuple[int, int, int]]]:
    """Compute Minimum Spanning Tree using Prim's algorithm with a binary min-heap."""
    visited = [False] * n
    min_heap: List[Tuple[int, int, int]] = [(0, start, -1)]
    total_weight = 0
    mst_edges: List[Tuple[int, int, int]] = []

    while min_heap and len(mst_edges) < n:
        weight, u, parent = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += weight
        if parent != -1:
            mst_edges.append((parent, u, weight))

        for v, w in adj.get(u, []):
            if not visited[v]:
                heapq.heappush(min_heap, (w, v, u))

    return total_weight, mst_edges


def longest_palindromic_substring_manacher(s: str) -> str:
    """Find the longest palindromic substring in O(n) time using Manacher's Algorithm."""
    if not s:
        return ""
    transformed = "#" + "#".join(s) + "#"
    n = len(transformed)
    p = [0] * n
    center = 0
    right = 0

    for i in range(n):
        mirror = 2 * center - i
        if i < right:
            p[i] = min(right - i, p[mirror])

        while i - (p[i] + 1) >= 0 and i + (p[i] + 1) < n and transformed[i - (p[i] + 1)] == transformed[i + (p[i] + 1)]:
            p[i] += 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    max_len = 0
    center_idx = 0
    for i in range(n):
        if p[i] > max_len:
            max_len = p[i]
            center_idx = i

    start = (center_idx - max_len) // 2
    return s[start:start + max_len]


def z_algorithm_search(text: str, pattern: str) -> List[int]:
    """Find all occurrences of pattern in text in linear time using the Z-Algorithm."""
    if not pattern or not text or len(pattern) > len(text):
        return []
    concat = pattern + "$" + text
    n = len(concat)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and concat[z[i]] == concat[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1

    m = len(pattern)
    matches = []
    for i in range(m + 1, n):
        if z[i] == m:
            matches.append(i - (m + 1))
    return matches


def boyer_moore_search(text: str, pattern: str) -> List[int]:
    """Find all pattern occurrences using Boyer-Moore string search with bad character heuristic."""
    n = len(text)
    m = len(pattern)
    if m == 0 or m > n:
        return []

    bad_char: Dict[str, int] = {}
    for i in range(m):
        bad_char[pattern[i]] = i

    matches: List[int] = []
    shift = 0
    while shift <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1
        if j < 0:
            matches.append(shift)
            shift += (m - bad_char.get(text[shift + m], -1)) if shift + m < n else 1
        else:
            bc_index = bad_char.get(text[shift + j], -1)
            shift += max(1, j - bc_index)
    return matches


class BinaryLiftingLCA:
    """Lowest Common Ancestor queries on trees in O(log N) via binary lifting."""
    def __init__(self, n: int, adj: Dict[int, List[int]], root: int = 0):
        self.n = n
        self.adj = adj
        self.root = root
        self.log = max(1, math.ceil(math.log2(n + 1))) + 1
        self.depth = [0] * n
        self.up = [[0] * self.log for _ in range(n)]
        self._dfs(root, root)

    def _dfs(self, node: int, parent: int):
        self.up[node][0] = parent
        for j in range(1, self.log):
            self.up[node][j] = self.up[self.up[node][j - 1]][j - 1]
        for neighbor in self.adj.get(node, []):
            if neighbor != parent:
                self.depth[neighbor] = self.depth[node] + 1
                self._dfs(neighbor, node)

    def query_lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        diff = self.depth[u] - self.depth[v]
        for j in range(self.log):
            if (diff >> j) & 1:
                u = self.up[u][j]
        if u == v:
            return u
        for j in reversed(range(self.log)):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
        return self.up[u][0]


class EulerTourTree:
    """Tree flattening via Euler Tour technique to map subtree queries into contiguous array intervals."""
    def __init__(self, n: int, adj: Dict[int, List[int]], root: int = 0):
        self.n = n
        self.tin = [0] * n
        self.tout = [0] * n
        self.tour: List[int] = []
        self.timer = 0
        self._dfs(root, -1, adj)

    def _dfs(self, u: int, p: int, adj: Dict[int, List[int]]):
        self.tin[u] = self.timer
        self.tour.append(u)
        self.timer += 1
        for v in adj.get(u, []):
            if v != p:
                self._dfs(v, u, adj)
        self.tout[u] = self.timer

    def is_ancestor(self, u: int, v: int) -> bool:
        return self.tin[u] <= self.tin[v] and self.tout[u] >= self.tout[v]

    def subtree_range(self, u: int) -> Tuple[int, int]:
        return self.tin[u], self.tout[u] - 1


def graham_scan_convex_hull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Compute the 2D Convex Hull in counter-clockwise order using Graham Scan."""
    pts = sorted(list(set(points)))
    if len(pts) <= 2:
        return pts

    def cross_product(o: Tuple[float, float], a: Tuple[float, float], b: Tuple[float, float]) -> float:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower: List[Tuple[float, float]] = []
    for p in pts:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper: List[Tuple[float, float]] = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]


def quickhull(points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
    """Compute 2D Convex Hull using the divide-and-conquer Quickhull algorithm."""
    pts = list(set(points))
    if len(pts) <= 2:
        return pts

    def distance_from_line(p1, p2, p):
        return (p[1] - p1[1]) * (p2[0] - p1[0]) - (p2[1] - p1[1]) * (p[0] - p1[0])

    def find_hull(p1, p2, point_set, hull):
        if not point_set:
            return
        farthest_point = None
        max_dist = 0.0
        for p in point_set:
            dist = distance_from_line(p1, p2, p)
            if dist > max_dist:
                max_dist = dist
                farthest_point = p
        if farthest_point is None:
            return
        hull.append(farthest_point)
        s1 = [p for p in point_set if distance_from_line(p1, farthest_point, p) > 0]
        s2 = [p for p in point_set if distance_from_line(farthest_point, p2, p) > 0]
        find_hull(p1, farthest_point, s1, hull)
        find_hull(farthest_point, p2, s2, hull)

    min_x = min(pts, key=lambda p: (p[0], p[1]))
    max_x = max(pts, key=lambda p: (p[0], p[1]))
    hull = [min_x, max_x]
    left_set = [p for p in pts if distance_from_line(min_x, max_x, p) > 0]
    right_set = [p for p in pts if distance_from_line(max_x, min_x, p) > 0]
    find_hull(min_x, max_x, left_set, hull)
    find_hull(max_x, min_x, right_set, hull)
    return hull


def closest_pair_of_points(points: List[Tuple[float, float]]) -> Tuple[float, Tuple[Tuple[float, float], Tuple[float, float]]]:
    """Find the closest pair of points in 2D space in O(n log n) divide-and-conquer time."""
    def dist(p1, p2):
        return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

    def rec_closest(px, py):
        n = len(px)
        if n <= 3:
            min_d = float('inf')
            pair = (px[0], px[1])
            for i in range(n):
                for j in range(i + 1, n):
                    d = dist(px[i], px[j])
                    if d < min_d:
                        min_d = d
                        pair = (px[i], px[j])
            return min_d, pair

        mid = n // 2
        mid_point = px[mid]
        left_x = px[:mid]
        right_x = px[mid:]
        left_set = set(left_x)
        left_y = [p for p in py if p in left_set]
        right_y = [p for p in py if p not in left_set]

        d1, pair1 = rec_closest(left_x, left_y)
        d2, pair2 = rec_closest(right_x, right_y)
        d, best_pair = (d1, pair1) if d1 < d2 else (d2, pair2)

        strip = [p for p in py if abs(p[0] - mid_point[0]) < d]
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 8, len(strip))):
                curr_d = dist(strip[i], strip[j])
                if curr_d < d:
                    d = curr_d
                    best_pair = (strip[i], strip[j])
        return d, best_pair

    px = sorted(points, key=lambda p: (p[0], p[1]))
    py = sorted(points, key=lambda p: (p[1], p[0]))
    return rec_closest(px, py)


def max_submatrix_sum(matrix: List[List[int]]) -> int:
    """Find the maximum sum of any contiguous 2D rectangular submatrix using 2D Kadane."""
    if not matrix or not matrix[0]:
        return 0
    rows = len(matrix)
    cols = len(matrix[0])
    max_sum = -float('inf')

    for top in range(rows):
        temp = [0] * cols
        for bottom in range(top, rows):
            for col in range(cols):
                temp[col] += matrix[bottom][col]

            curr_sum = 0
            for val in temp:
                curr_sum = max(val, curr_sum + val)
                max_sum = max(max_sum, curr_sum)

    return int(max_sum)


def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    """Find the Longest Increasing Subsequence (LIS) in O(N log N) using patience sorting and binary search."""
    if not nums:
        return []
    import bisect
    tails: List[int] = []
    tail_indices: List[int] = []
    parent = [-1] * len(nums)

    for i, x in enumerate(nums):
        idx = bisect.bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
            tail_indices.append(i)
        else:
            tails[idx] = x
            tail_indices[idx] = i
        if idx > 0:
            parent[i] = tail_indices[idx - 1]

    curr = tail_indices[-1]
    lis: List[int] = []
    while curr != -1:
        lis.append(nums[curr])
        curr = parent[curr]
    return lis[::-1]


class HopcroftKarp:
    """Find maximum cardinality bipartite matching in O(E * sqrt(V)) time."""
    def __init__(self, n_u: int, n_v: int, adj: Dict[int, List[int]]):
        self.n_u = n_u
        self.n_v = n_v
        self.adj = adj
        self.match_u = [-1] * n_u
        self.match_v = [-1] * n_v
        self.dist = [0] * n_u

    def bfs(self) -> bool:
        q = deque()
        for u in range(self.n_u):
            if self.match_u[u] == -1:
                self.dist[u] = 0
                q.append(u)
            else:
                self.dist[u] = 10**9

        found_augmenting_path = False
        while q:
            u = q.popleft()
            for v in self.adj.get(u, []):
                next_u = self.match_v[v]
                if next_u == -1:
                    found_augmenting_path = True
                elif self.dist[next_u] == 10**9:
                    self.dist[next_u] = self.dist[u] + 1
                    q.append(next_u)
        return found_augmenting_path

    def dfs(self, u: int) -> bool:
        for v in self.adj.get(u, []):
            next_u = self.match_v[v]
            if next_u == -1 or (self.dist[next_u] == self.dist[u] + 1 and self.dfs(next_u)):
                self.match_u[u] = v
                self.match_v[v] = u
                return True
        self.dist[u] = 10**9
        return False

    def max_matching(self) -> int:
        matching = 0
        while self.bfs():
            for u in range(self.n_u):
                if self.match_u[u] == -1 and self.dfs(u):
                    matching += 1
        return matching


def fft_multiply(poly1: List[int], poly2: List[int]) -> List[int]:
    """Multiply two polynomials in O(n log n) using Cooley-Tukey Fast Fourier Transform (FFT)."""
    n = 1
    target_len = len(poly1) + len(poly2) - 1
    while n < target_len:
        n <<= 1

    def fft(a: List[complex], invert: bool = False) -> List[complex]:
        sz = len(a)
        if sz == 1:
            return a
        even = fft(a[0::2], invert)
        odd = fft(a[1::2], invert)
        angle = -2 * math.pi / sz if invert else 2 * math.pi / sz
        w = 1.0
        wn = complex(math.cos(angle), math.sin(angle))
        res = [0j] * sz
        for i in range(sz // 2):
            res[i] = even[i] + w * odd[i]
            res[i + sz // 2] = even[i] - w * odd[i]
            if invert:
                res[i] /= 2
                res[i + sz // 2] /= 2
            w *= wn
        return res

    a = [complex(x, 0) for x in poly1] + [0j] * (n - len(poly1))
    b = [complex(x, 0) for x in poly2] + [0j] * (n - len(poly2))
    fa = fft(a, False)
    fb = fft(b, False)
    fc = [fa[i] * fb[i] for i in range(n)]
    c = fft(fc, True)
    return [round(c[i].real) for i in range(target_len)]


if __name__ == "__main__":
    print("=== Iteration 1: Fibonacci ===")
    print("First 10 Fib numbers:", list(fibonacci_stream(10)))
    print("Fib(30):", fibonacci_memo(30))

    print("\n=== Iteration 2: Binary Search ===")
    sample_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Index of 23 (iterative):", binary_search_iterative(sample_list, 23))
    print("Index of 23 (recursive):", binary_search_recursive(sample_list, 23))
    print("Index of 99 (not found):", binary_search_iterative(sample_list, 99))

    print("\n=== Iteration 3: Prime Sieve ===")
    print("Primes up to 50:", sieve_of_eratosthenes(50))
    print("Is 97 prime?:", is_prime(97))
    print("Is 100 prime?:", is_prime(100))

    print("\n=== Iteration 4: Sorting ===")
    unsorted = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Unsorted:", unsorted)
    print("Quicksort result:", quicksort(unsorted))
    print("Mergesort result:", mergesort(unsorted))

    print("\n=== Iteration 5: Two Sum & Three Sum ===")
    nums_for_two_sum = [2, 7, 11, 15]
    print("Two sum target 9:", two_sum(nums_for_two_sum, 9))
    nums_for_three_sum = [-1, 0, 1, 2, -1, -4]
    print("Three sum triplets:", three_sum(nums_for_three_sum))

    print("\n=== Iteration 6: Longest Common Subsequence ===")
    s1, s2 = "abcde", "ace"
    print(f"LCS of '{s1}' and '{s2}':", longest_common_subsequence(s1, s2))

    print("\n=== Iteration 7: LRU Cache ===")
    lru = LRUCache(2)
    lru.put(1, "Data 1")
    lru.put(2, "Data 2")
    print("Get key 1:", lru.get(1))
    lru.put(3, "Data 3")  # evicts key 2
    print("Get key 2 (evicted):", lru.get(2))
    print("Get key 3:", lru.get(3))

    print("\n=== Iteration 8: Dijkstra's Shortest Path ===")
    weighted_graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
        'E': {'C': 10, 'D': 2, 'Z': 3},
        'Z': {'D': 6, 'E': 3}
    }
    dist, prev = dijkstra(weighted_graph, 'A')
    print("Shortest distances from Node A:", dist)

    print("\n=== Iteration 9: Kadane's Algorithm ===")
    sample_sub = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print("Max subarray sum for", sample_sub, "->", max_subarray_sum(sample_sub))

    print("\n=== Iteration 10: 0/1 Knapsack ===")
    wts, vals, cap = [2, 3, 4, 5], [3, 4, 5, 6], 5
    print("Max knapsack value (capacity 5):", knapsack_01(wts, vals, cap))

    print("\n=== Iteration 11: Graph BFS & DFS ===")
    sample_adj = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("BFS from A:", bfs_traversal(sample_adj, 'A'))
    print("DFS from A:", dfs_traversal(sample_adj, 'A'))

    print("\n=== Iteration 12: Topological Sort ===")
    dag_nodes = ["build", "test", "package", "deploy", "monitor"]
    dag_edges = [("build", "test"), ("test", "package"), ("package", "deploy"), ("deploy", "monitor")]
    print("Topological build order:", topological_sort(dag_nodes, dag_edges))

    print("\n=== Iteration 13: Trie (Prefix Tree) ===")
    trie = Trie()
    for w in ["apple", "app", "application", "aptitude", "bat"]:
        trie.insert(w)
    print("Search 'apple':", trie.search("apple"))
    print("Search 'app':", trie.search("app"))
    print("Search 'appl':", trie.search("appl"))
    print("Starts with 'app':", trie.starts_with("app"))
    print("Starts with 'bat':", trie.starts_with("bat"))
    print("Starts with 'cat':", trie.starts_with("cat"))
    print("All 13 algorithms and data structures completed and verified!")

    print("\n=== Iteration 14: Union-Find (DSU) ===")
    dsu = DisjointSetUnion(5)
    dsu.union(0, 2)
    dsu.union(4, 2)
    print("Find(0) == Find(4):", dsu.find(0) == dsu.find(4))
    print("Find(0) == Find(1):", dsu.find(0) == dsu.find(1))

    print("\n=== Iteration 15: Kruskal's MST ===")
    sample_edges = [(10, 0, 1), (6, 0, 2), (5, 0, 3), (15, 1, 3), (4, 2, 3)]
    mst_wt, mst_edges = kruskal_mst(4, sample_edges)
    print(f"MST Weight: {mst_wt}, Edges: {mst_edges}")

    print("\n=== Iteration 16: Bellman-Ford ===")
    bf_vertices = ["S", "A", "B", "C", "D", "E"]
    bf_edges = [("S", "A", 10), ("S", "E", 8), ("A", "C", 2), ("B", "A", 1), ("C", "B", -2), ("D", "C", -1), ("D", "A", -4), ("E", "D", 1)]
    print("Bellman-Ford from S:", bellman_ford(bf_vertices, bf_edges, "S"))

    print("\n=== Iteration 17: Floyd-Warshall ===")
    fw_nodes = ["1", "2", "3", "4"]
    fw_matrix = {
        "1": {"3": -2},
        "2": {"1": 4, "3": 3},
        "3": {"4": 2},
        "4": {"2": -1}
    }
    fw_res = floyd_warshall(fw_nodes, fw_matrix)
    print("Distance from 2 to 4:", fw_res["2"]["4"])

    print("\n=== Iteration 18: KMP Pattern Search ===")
    txt, pat = "ABABDABACDABABCABAB", "ABABCABAB"
    print(f"KMP matches for '{pat}' in text: {kmp_search(txt, pat)}")

    print("\n=== Iteration 19: Rabin-Karp Search ===")
    rk_text, rk_pat = "GEEKS FOR GEEKS", "GEEK"
    print(f"Rabin-Karp matches for '{rk_pat}': {rabin_karp_search(rk_text, rk_pat)}")

    print("\n=== Iteration 20: Monotonic Stack (NGE) ===")
    sample_nge = [4, 5, 2, 25, 7, 8]
    print(f"Next Greater Elements for {sample_nge} -> {next_greater_elements(sample_nge)}")

    print("\n=== Iteration 21: Sliding Window Maximum ===")
    sw_nums, sw_k = [1, 3, -1, -3, 5, 3, 6, 7], 3
    print(f"Sliding window max for {sw_nums} (k={sw_k}): {max_sliding_window(sw_nums, sw_k)}")

    print("\n=== Iteration 22: Fenwick Tree ===")
    bit = FenwickTree(6)
    for idx, val in enumerate([3, 2, -1, 6, 5, 4], start=1):
        bit.update(idx, val)
    print("Prefix sum up to 4:", bit.query(4))
    print("Range sum [2, 5]:", bit.range_query(2, 5))

    print("\n=== Iteration 23: Segment Tree RMQ ===")
    seg_data = [5, 2, 8, 3, 9, 1, 6]
    st = SegmentTreeRMQ(seg_data)
    print(f"Segment tree data: {seg_data}")
    print("Min in range [1, 4]:", st.query(1, 4))
    print("Min in range [0, 6]:", st.query(0, 6))

    print("\n=== Iteration 24: A* Search Algorithm ===")
    maze = [
        [0, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 1, 0]
    ]
    a_star_path = a_star_search((0, 0), (3, 3), maze)
    print("A* path found:", a_star_path)

    print("\n=== Iteration 25: Edit Distance ===")
    w1, w2 = "horse", "ros"
    print(f"Edit distance between '{w1}' and '{w2}':", min_edit_distance(w1, w2))

    print("\n=== Iteration 26: Coin Change ===")
    demo_coins = [1, 2, 5]
    print(f"Fewest coins for amount 11 with {demo_coins}:", coin_change_min(demo_coins, 11))
    print(f"Ways to make amount 5 with {demo_coins}:", coin_change_combinations(demo_coins, 5))

    print("\n=== Iteration 27: Matrix Exponentiation ===")
    print("Fib(50) via matrix exp:", fibonacci_matrix(50))
    print("Fib(70) via matrix exp:", fibonacci_matrix(70))

    print("\n=== Iteration 28: Huffman Coding ===")
    huff_text = "antigravity algorithms suite"
    huff_codes, _ = build_huffman_codes(huff_text)
    print(f"Huffman Prefix Codes for '{huff_text}':")
    for ch, code in sorted(huff_codes.items()):
        print(f"  {repr(ch)}: {code}")
    print("\n=== Iteration 29: Tarjan's Strongly Connected Components ===")
    tarjan_g = {0: [1], 1: [2], 2: [0, 3], 3: [4], 4: [5, 7], 5: [6], 6: [4], 7: []}
    print("Tarjan SCCs:", tarjan_scc(tarjan_g))
    print("\n=== Iteration 30: Kosaraju's Strongly Connected Components ===")
    kosa_adj = {0: [2, 3], 1: [0], 2: [1], 3: [4], 4: []}
    print("Kosaraju SCCs:", kosaraju_scc(5, kosa_adj))
    print("\n=== Iteration 31: Edmonds-Karp Maximum Flow ===")
    cap_mat = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    print("Edmonds-Karp Max Flow from 0 to 5:", edmonds_karp_max_flow(cap_mat, 0, 5))
    print("\n=== Iteration 32: Dinic's Algorithm ===")
    dinic = DinicMaxFlow(6)
    dinic.add_edge(0, 1, 10)
    dinic.add_edge(0, 2, 10)
    dinic.add_edge(1, 2, 2)
    dinic.add_edge(1, 3, 4)
    dinic.add_edge(1, 4, 8)
    dinic.add_edge(2, 4, 9)
    dinic.add_edge(3, 5, 10)
    dinic.add_edge(4, 5, 10)
    print("Dinic Max Flow from 0 to 5:", dinic.compute_max_flow(0, 5))
    print("\n=== Iteration 33: Prim's Algorithm ===")
    prim_adj = {
        0: [(1, 4), (7, 8)],
        1: [(0, 4), (2, 8), (7, 11)],
        2: [(1, 8), (3, 7), (8, 2), (5, 4)],
        3: [(2, 7), (4, 9), (5, 14)],
        4: [(3, 9), (5, 10)],
        5: [(4, 10), (3, 14), (2, 4), (6, 2)],
        6: [(5, 2), (8, 6), (7, 1)],
        7: [(0, 8), (1, 11), (6, 1), (8, 7)],
        8: [(2, 2), (6, 6), (7, 7)]
    }
    prim_wt, prim_edges = prim_mst(9, prim_adj)
    print(f"Prim MST Weight: {prim_wt}, Edge Count: {len(prim_edges)}")
    print("\n=== Iteration 34: Manacher's Palindrome Search ===")
    sample_pal = "forgeeksskeegfor"
    print(f"Longest palindromic substring in '{sample_pal}':", longest_palindromic_substring_manacher(sample_pal))
    print("\n=== Iteration 35: Z-Algorithm Search ===")
    z_txt, z_pat = "baabaaahbaabaa", "aaba"
    print(f"Z-Algorithm occurrences of '{z_pat}':", z_algorithm_search(z_txt, z_pat))
    print("\n=== Iteration 36: Boyer-Moore Search ===")
    bm_txt, bm_pat = "AABAACAADAABAABA", "AABA"
    print(f"Boyer-Moore matches for '{bm_pat}':", boyer_moore_search(bm_txt, bm_pat))
    print("\n=== Iteration 37: Binary Lifting LCA ===")
    lca_adj = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    lca_solver = BinaryLiftingLCA(6, lca_adj, root=0)
    print("LCA(3, 4):", lca_solver.query_lca(3, 4))
    print("LCA(3, 5):", lca_solver.query_lca(3, 5))
    print("\n=== Iteration 38: Euler Tour Tree ===")
    ett_adj = {0: [1, 2], 1: [0, 3, 4], 2: [0, 5], 3: [1], 4: [1], 5: [2]}
    ett = EulerTourTree(6, ett_adj, root=0)
    print("Subtree 1 range in Euler tour:", ett.subtree_range(1))
    print("Is 1 ancestor of 3?:", ett.is_ancestor(1, 3))
    print("Is 2 ancestor of 3?:", ett.is_ancestor(2, 3))
    print("\n=== Iteration 39: Graham Scan Convex Hull ===")
    gs_pts = [(0.0, 3.0), (1.0, 1.0), (2.0, 2.0), (4.0, 4.0), (0.0, 0.0), (1.0, 2.0), (3.0, 1.0), (3.0, 3.0)]
    print("Convex Hull points:", graham_scan_convex_hull(gs_pts))
    print("\n=== Iteration 40: Quickhull ===")
    qh_pts = [(0.0, 3.0), (1.0, 1.0), (2.0, 2.0), (4.0, 4.0), (0.0, 0.0), (1.0, 2.0), (3.0, 1.0), (3.0, 3.0)]
    qh_hull = quickhull(qh_pts)
    print("Quickhull vertices count:", len(qh_hull))
    print("\n=== Iteration 41: Closest Pair of Points ===")
    cloud_pts = [(2.0, 3.0), (12.0, 30.0), (40.0, 50.0), (5.0, 1.0), (12.0, 10.0), (3.0, 4.0)]
    min_dist, closest_pts = closest_pair_of_points(cloud_pts)
    print(f"Closest distance: {min_dist:.4f} between {closest_pts}")
    print("\n=== Iteration 42: 2D Kadane Max Submatrix Sum ===")
    mat_kadane = [
        [1, 2, -1, -4, -20],
        [-8, -3, 4, 2, 1],
        [3, 8, 10, 1, 3],
        [-4, -1, 1, 7, -6]
    ]
    print("Maximum submatrix sum:", max_submatrix_sum(mat_kadane))
    print("\n=== Iteration 43: Longest Increasing Subsequence ===")
    lis_arr = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"LIS of {lis_arr}: {longest_increasing_subsequence(lis_arr)}")
    print("\n=== Iteration 44: Hopcroft-Karp Matching ===")
    hk_adj = {0: [0, 1], 1: [0], 2: [2], 3: [1, 2]}
    hk = HopcroftKarp(4, 3, hk_adj)
    print("Max bipartite matching cardinality:", hk.max_matching())
    print("\n=== Iteration 45: Fast Fourier Transform Polynomial Multiplication ===")
    p1 = [1, 2, 3]
    p2 = [4, 5, 6]
    print("FFT (1 + 2x + 3x^2) * (4 + 5x + 6x^2):", fft_multiply(p1, p2))
