"""
Algorithms & Data Structures Collection
Part 1: Fibonacci Numbers with Memoization
"""

from typing import Generator, Dict


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


if __name__ == "__main__":
    print("=== Iteration 1: Fibonacci ===")
    print("First 10 Fib numbers:", list(fibonacci_stream(10)))
    print("Fib(30):", fibonacci_memo(30))
