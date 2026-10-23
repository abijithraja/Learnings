"""
Algorithms & Data Structures Collection
Part 1: Fibonacci Numbers with Memoization
Part 2: Binary Search (Iterative & Recursive)
Part 3: Sieve of Eratosthenes & Prime Verification
"""

from typing import Generator, Dict, List, Optional
import math


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
