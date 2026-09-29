"""
Practice 1: Recursion
=====================
This module implements recursive Factorial and Fibonacci functions.
"""


def factorial(n):
    """
    Compute the factorial of n recursively.
    n! = n * (n-1) * (n-2) * ... * 1
    Base case: 0! = 1, 1! = 1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """
    Compute the nth Fibonacci number recursively.
    fib(0) = 0, fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n >= 2
    """
    if n < 0:
        raise ValueError("Fibonacci is not defined for negative numbers.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Demonstrate recursive Factorial and Fibonacci."""
    print("=== Factorial ===")
    for i in range(6):
        print(f"{i}! = {factorial(i)}")

    print("\n=== Fibonacci ===")
    for i in range(10):
        print(f"fib({i}) = {fibonacci(i)}")

    # Test edge cases
    print("\n=== Edge Cases ===")
    try:
        factorial(-1)
    except ValueError as e:
        print(f"factorial(-1): {e}")

    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"fibonacci(-1): {e}")


if __name__ == "__main__":
    main()