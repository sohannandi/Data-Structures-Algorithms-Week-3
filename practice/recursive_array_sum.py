"""
Practice 5: Recursive Array Sum
===============================
This module implements a recursive function that returns the sum of all
elements in an array.
"""


def recursive_array_sum(arr, index=0):
    """
    Recursively compute the sum of all elements in an array.

    Args:
        arr: List of numbers
        index: Current index being processed (default 0 for start)

    Returns:
        Sum of all elements in the array

    Base case: When index reaches the end of array, return 0
    Recursive case: arr[index] + recursive_array_sum(arr, index + 1)
    """
    # Base case: if we've processed all elements
    if index >= len(arr):
        return 0

    # Recursive case: current element + sum of remaining elements
    return arr[index] + recursive_array_sum(arr, index + 1)


def recursive_array_sum_slice(arr):
    """
    Alternative implementation using array slicing.
    Less efficient due to creating new arrays, but conceptually simple.

    Base case: Empty array has sum 0
    Recursive case: first element + sum of rest of array
    """
    # Base case
    if len(arr) == 0:
        return 0

    # Recursive case
    return arr[0] + recursive_array_sum_slice(arr[1:])


def main():
    """Demonstrate recursive array sum."""
    # Test cases
    test_arrays = [
        [],                           # Empty array
        [5],                          # Single element
        [1, 2, 3, 4, 5],              # Simple sequence
        [10, 20, 30],                 # Multiples of 10
        [-1, 0, 1],                   # With negative and zero
        [100, 200, 300, 400, 500],    # Larger numbers
    ]

    print("=== Recursive Array Sum (index-based) ===")
    for arr in test_arrays:
        result = recursive_array_sum(arr)
        print(f"Sum of {arr} = {result}")

    print("\n=== Recursive Array Sum (slice-based) ===")
    for arr in test_arrays:
        result = recursive_array_sum_slice(arr)
        print(f"Sum of {arr} = {result}")

    # Verification with built-in sum
    print("\n=== Verification with built-in sum ===")
    for arr in test_arrays:
        recursive_result = recursive_array_sum(arr)
        builtin_result = sum(arr)
        match = "PASS" if recursive_result == builtin_result else "FAIL"
        print(f"[{match}] {arr}: recursive={recursive_result}, builtin={builtin_result}")


if __name__ == "__main__":
    main()