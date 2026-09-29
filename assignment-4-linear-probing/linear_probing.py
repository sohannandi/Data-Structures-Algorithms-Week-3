"""
Assignment 4: Hash Table with Linear Probing
============================================
This module implements collision handling in a hash table using Linear Probing.
Supports insert and display operations.
"""


class HashTableLinearProbing:
    """Hash table implementation using linear probing for collision resolution."""

    def __init__(self, size=10):
        """Initialize the hash table with a fixed size."""
        self.size = size
        # Each slot can hold one value or None (empty) or a special marker for deleted
        self.table = [None] * self.size
        # Special marker for deleted slots (to distinguish from never-used slots)
        self.DELETED = object()

    def _hash_function(self, key):
        """
        Convert key into a valid table index.
        Using modulo operation: hash(key) = key % size
        """
        return key % self.size

    def insert(self, key):
        """
        Insert a value into the hash table using linear probing.
        Detects collisions and resolves them by checking the next available position.
        """
        index = self._hash_function(key)
        original_index = index

        # Probe until we find an empty slot or a deleted slot
        while self.table[index] is not None and self.table[index] is not self.DELETED:
            # Collision detected - move to next slot
            index = (index + 1) % self.size

            # If we've checked all slots and returned to start, table is full
            if index == original_index:
                raise Exception("Hash table is full")

        # Found an empty slot (or deleted slot), insert the key
        self.table[index] = key

    def search(self, key):
        """
        Search for a key in the hash table.
        Returns True if found, False otherwise.
        """
        index = self._hash_function(key)
        original_index = index

        # Probe until we find the key or an empty slot (never-used)
        while self.table[index] is not None:
            if self.table[index] is not self.DELETED and self.table[index] == key:
                return True
            index = (index + 1) % self.size

            # If we've checked all slots and returned to start, key is not present
            if index == original_index:
                break

        return False

    def delete(self, key):
        """
        Delete a key from the hash table.
        Marks the slot as deleted (using special marker) rather than setting to None
        to maintain the integrity of linear probing chains.
        """
        index = self._hash_function(key)
        original_index = index

        # Probe until we find the key or an empty slot
        while self.table[index] is not None:
            if self.table[index] is not self.DELETED and self.table[index] == key:
                self.table[index] = self.DELETED  # Mark as deleted
                return True
            index = (index + 1) % self.size

            # If we've checked all slots and returned to start, key not found
            if index == original_index:
                break

        return False

    def display(self):
        """Display the hash table contents."""
        print("Hash Table Contents (Linear Probing):")
        for i, value in enumerate(self.table):
            if value is None:
                print(f"  Index {i}: Empty")
            elif value is self.DELETED:
                print(f"  Index {i}: Deleted")
            else:
                print(f"  Index {i}: {value}")


def main():
    """Demonstrate hash table with linear probing."""
    # Create hash table with size 10 as in the example
    ht = HashTableLinearProbing(size=10)

    # Example from PRD demonstrating collision
    print("Inserting 25 (should go to index 5: 25 % 10 = 5)")
    ht.insert(25)

    print("Inserting 35 (collision at index 5, should go to index 6)")
    ht.insert(35)

    # Additional test cases
    print("\n--- Additional insertions ---")
    ht.insert(45)  # Should go to index 7 (collision chain: 5->6->7)
    ht.insert(55)  # Should go to index 8
    ht.insert(65)  # Should go to index 9
    ht.insert(75)  # Should wrap around to index 0
    ht.insert(85)  # Should go to index 1
    ht.insert(95)  # Should go to index 2

    print(f"\nSearch for 35: {ht.search(35)}")
    print(f"Search for 99: {ht.search(99)}")

    ht.display()

    # Test deletion
    print("\n--- Testing deletion ---")
    print("Deleting 35")
    ht.delete(35)
    print(f"Search for 35 after deletion: {ht.search(35)}")
    ht.display()

    # Test edge case: trying to insert into full table
    print("\n--- Testing full table ---")
    # Create a fresh table and fill it completely
    ht_full = HashTableLinearProbing(size=10)
    for i in range(10):
        ht_full.insert(i * 10)  # Insert 0, 10, 20, ..., 90

    print("Filled table with 10 elements (0, 10, 20, ..., 90):")
    ht_full.display()

    try:
        # Table should be full now
        ht_full.insert(1001)
        print("Insertion succeeded unexpectedly")
    except Exception as e:
        print(f"Expected error: {e}")


if __name__ == "__main__":
    main()