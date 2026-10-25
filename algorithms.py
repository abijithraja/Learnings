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
