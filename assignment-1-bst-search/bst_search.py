"""
Assignment 1: Binary Search Tree Search
========================================
This module implements a Binary Search Tree that supports insertion
and searching for a specified value.
"""


class BSTNode:
    """A node in the Binary Search Tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with insert and search operations."""

    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert a value into the BST."""
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """Recursively find the correct position and insert the value."""
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert_recursive(node.right, value)
        # If value == node.value, we do nothing (duplicates are ignored)
        # This is a clear policy: duplicates are not stored

    def search(self, value):
        """
        Search for a value in the BST.
        Returns True if found, False otherwise.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """Recursively search for a value following BST ordering rules."""
        if node is None:
            return False

        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


def main():
    """Demonstrate BST insert and search functionality."""
    bst = BinarySearchTree()

    # Insert values from the example
    print("Inserting: 50, 30, 70, 20, 40, 60, 80")
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)

    # Search for existing value
    search_val = 40
    if bst.search(search_val):
        print(f"{search_val} found")
    else:
        print(f"{search_val} not found")

    # Search for non-existing value
    search_val = 90
    if bst.search(search_val):
        print(f"{search_val} found")
    else:
        print(f"{search_val} not found")

    # Test with duplicates
    print("\n--- Testing duplicate handling ---")
    bst.insert(40)  # Duplicate
    bst.insert(40)  # Duplicate
    if bst.search(40):
        print("40 still found (duplicates ignored)")


if __name__ == "__main__":
    main()