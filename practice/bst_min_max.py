"""
Practice 4: BST Minimum and Maximum
====================================
This module implements finding the minimum and maximum values in a BST
using BST properties.
"""


class BSTNode:
    """A node in the Binary Search Tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with min/max operations."""

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
        # If value == node.value, duplicates are ignored

    def find_min(self):
        """
        Find the minimum value in the BST using BST properties.
        The minimum is the leftmost node.
        Returns None if tree is empty.
        """
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        """
        Find the maximum value in the BST using BST properties.
        The maximum is the rightmost node.
        Returns None if tree is empty.
        """
        if self.root is None:
            return None

        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def display(self):
        """Display the BST using inorder traversal (sorted order)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursively perform inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)


def main():
    """Demonstrate BST minimum and maximum finding."""
    bst = BinarySearchTree()

    # Insert values to create a test tree
    values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]
    print("Inserting values:", values)
    for val in values:
        bst.insert(val)

    # Display BST in sorted order
    print(f"BST inorder (sorted): {bst.display()}")

    # Find min and max
    min_val = bst.find_min()
    max_val = bst.find_max()

    print(f"\nMinimum value: {min_val}")
    print(f"Maximum value: {max_val}")

    # Verify using properties
    print(f"\nVerification:")
    print(f"Leftmost node value: {min_val} (should be 10)")
    print(f"Rightmost node value: {max_val} (should be 80)")

    # Test edge cases
    print("\n=== Edge Cases ===")

    # Empty tree
    empty_bst = BinarySearchTree()
    print(f"Empty tree - Min: {empty_bst.find_min()}, Max: {empty_bst.find_max()}")

    # Single node
    single_bst = BinarySearchTree()
    single_bst.insert(42)
    print(f"Single node tree - Min: {single_bst.find_min()}, Max: {single_bst.find_max()}")

    # Already sorted insertion (creates a skewed tree)
    skewed_bst = BinarySearchTree()
    sorted_values = [1, 2, 3, 4, 5]
    print(f"\nInserting sorted values: {sorted_values}")
    for val in sorted_values:
        skewed_bst.insert(val)
    print(f"Skewed BST inorder: {skewed_bst.display()}")
    print(f"Skewed tree - Min: {skewed_bst.find_min()}, Max: {skewed_bst.find_max()}")


if __name__ == "__main__":
    main()