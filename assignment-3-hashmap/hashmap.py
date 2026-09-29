"""
Assignment 3: HashMap Using Arrays
==================================
This module implements a basic HashMap using an array-based storage structure.
Supports put(key, value) and get(key) operations.
"""


class HashMap:
    """A simple HashMap implementation using array-based storage."""

    def __init__(self, size=10):
        """Initialize the hash table with a fixed size."""
        self.size = size
        # Each bucket stores a list of (key, value) tuples to handle collisions
        # (though for this assignment, we'll implement simple linear probing in Assignment 4)
        # For Assignment 3, we'll use separate chaining with lists
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        """
        Convert key into a valid table index.
        Using modulo operation as specified in the example: hash(key) = key % 10
        """
        return key % self.size

    def put(self, key, value):
        """
        Store a key-value pair.
        Handles collisions using separate chaining.
        """
        index = self._hash_function(key)
        bucket = self.table[index]

        # Check if key already exists, update if so
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing
                return

        # Key doesn't exist, append new key-value pair
        bucket.append((key, value))

    def get(self, key):
        """
        Retrieve value using key.
        Returns None if key is not present.
        """
        index = self._hash_function(key)
        bucket = self.table[index]

        # Search for key in the bucket
        for k, v in bucket:
            if k == key:
                return v

        # Key not found
        return None

    def display(self):
        """Display the hash table contents for debugging."""
        print("Hash Table Contents:")
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"  Index {i}: {bucket}")
            else:
                print(f"  Index {i}: []")


def main():
    """Demonstrate HashMap functionality."""
    # Create HashMap with size 10 as in the example
    hashmap = HashMap(size=10)

    # Example from PRD
    print("Putting (25, 'Sohan')")
    hashmap.put(25, "Sohan")

    result = hashmap.get(25)
    print(f"Getting key 25: {result}")

    # Additional test cases
    print("\n--- Additional tests ---")
    hashmap.put(35, "Rahul")  # Will collide with 25 at index 5
    hashmap.put(45, "Amit")   # Will also collide at index 5
    hashmap.put(15, "Priya")  # Different index

    print(f"Getting key 35: {hashmap.get(35)}")
    print(f"Getting key 45: {hashmap.get(45)}")
    print(f"Getting key 15: {hashmap.get(15)}")
    print(f"Getting key 99 (missing): {hashmap.get(99)}")

    hashmap.display()


if __name__ == "__main__":
    main()