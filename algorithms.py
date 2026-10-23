"""
Algorithms & Data Structures Collection
Part 1: Fibonacci Numbers with Memoization
Part 2: Binary Search (Iterative & Recursive)
"""

from typing import Generator, Dict, List, Optional


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


if __name__ == "__main__":
    print("=== Iteration 1: Fibonacci ===")
    print("First 10 Fib numbers:", list(fibonacci_stream(10)))
    print("Fib(30):", fibonacci_memo(30))

    print("\n=== Iteration 2: Binary Search ===")
    sample_list = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print("Index of 23 (iterative):", binary_search_iterative(sample_list, 23))
    print("Index of 23 (recursive):", binary_search_recursive(sample_list, 23))
    print("Index of 99 (not found):", binary_search_iterative(sample_list, 99))
