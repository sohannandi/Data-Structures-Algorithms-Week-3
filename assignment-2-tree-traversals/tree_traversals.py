"""
Assignment 2: Recursive Tree Traversals
========================================
This module implements the three standard recursive binary-tree traversals:
- Inorder
- Preorder
- Postorder
"""


class BSTNode:
    """A node in the Binary Search Tree."""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary Search Tree with traversal operations."""

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

    def inorder(self):
        """Return list of values from inorder traversal (Left, Root, Right)."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursively perform inorder traversal."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder(self):
        """Return list of values from preorder traversal (Root, Left, Right)."""
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        """Recursively perform preorder traversal."""
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder(self):
        """Return list of values from postorder traversal (Left, Right, Root)."""
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        """Recursively perform postorder traversal."""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)


def build_example_tree():
    r"""Build the example tree from the PRD:
            50
           /  \
         30    70
        / \    / \
       20 40  60 80
    """
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.insert(val)
    return bst


def main():
    """Demonstrate all three recursive traversals."""
    bst = build_example_tree()

    # Perform traversals
    inorder_result = bst.inorder()
    preorder_result = bst.preorder()
    postorder_result = bst.postorder()

    # Display results
    print("Inorder:  ", " ".join(map(str, inorder_result)))
    print("Preorder: ", " ".join(map(str, preorder_result)))
    print("Postorder:", " ".join(map(str, postorder_result)))

    # Test empty tree
    print("\n--- Testing empty tree ---")
    empty_bst = BinarySearchTree()
    print(f"Inorder:  {empty_bst.inorder()}")
    print(f"Preorder: {empty_bst.preorder()}")
    print(f"Postorder: {empty_bst.postorder()}")


if __name__ == "__main__":
    main()