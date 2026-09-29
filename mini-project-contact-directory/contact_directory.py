"""
Mini Project: Contact Directory
==================================
This module implements a Contact Directory using a Binary Search Tree.
The BST is organized using the contact's name as the key.

Each contact contains:
- Name (key for BST ordering)
- Phone Number

The system supports:
1. Add Contact
2. Search Contact
3. Delete Contact
4. Display All Contacts (alphabetical order via inorder traversal)
"""


class ContactNode:
    """A node in the Contact BST."""

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class ContactDirectory:
    """Contact Directory implemented using a Binary Search Tree."""

    def __init__(self):
        self.root = None

    def add_contact(self, name, phone):
        """
        Add a new contact to the directory.
        Handles duplicate names by updating the phone number.
        """
        if self.root is None:
            self.root = ContactNode(name, phone)
            return True
        else:
            return self._insert_recursive(self.root, name, phone)

    def _insert_recursive(self, node, name, phone):
        """Recursively find the correct position and insert the contact."""
        if name < node.name:
            if node.left is None:
                node.left = ContactNode(name, phone)
                return True
            else:
                return self._insert_recursive(node.left, name, phone)
        elif name > node.name:
            if node.right is None:
                node.right = ContactNode(name, phone)
                return True
            else:
                return self._insert_recursive(node.right, name, phone)
        else:
            # Duplicate name found - update phone number (defined behavior)
            node.phone = phone
            return False  # Indicates duplicate was updated, not inserted

    def search_contact(self, name):
        """
        Search for a contact by name.
        Returns (name, phone) tuple if found, None otherwise.
        """
        return self._search_recursive(self.root, name)

    def _search_recursive(self, node, name):
        """Recursively search for a contact following BST ordering."""
        if node is None:
            return None

        if name == node.name:
            return (node.name, node.phone)
        elif name < node.name:
            return self._search_recursive(node.left, name)
        else:
            return self._search_recursive(node.right, name)

    def delete_contact(self, name):
        """
        Delete a contact by name.
        Handles all three BST deletion cases:
        1. Node is a leaf
        2. Node has one child
        3. Node has two children (replaces with inorder successor)
        Returns True if deleted, False if not found.
        """
        if self.root is None:
            return False

        self.root, deleted = self._delete_recursive(self.root, name)
        return deleted

    def _delete_recursive(self, node, name):
        """Recursively delete a contact, handling all three BST deletion cases."""
        if node is None:
            return node, False  # Contact not found

        if name < node.name:
            node.left, deleted = self._delete_recursive(node.left, name)
            return node, deleted
        elif name > node.name:
            node.right, deleted = self._delete_recursive(node.right, name)
            return node, deleted
        else:
            # Node to delete found
            # Case 1: Node is a leaf (no children)
            if node.left is None and node.right is None:
                return None, True

            # Case 2: Node has one child (right child only)
            elif node.left is None:
                return node.right, True

            # Case 2: Node has one child (left child only)
            elif node.right is None:
                return node.left, True

            # Case 3: Node has two children
            else:
                # Find inorder successor (minimum value in right subtree)
                successor = self._find_min(node.right)
                # Copy successor's data to current node
                node.name = successor.name
                node.phone = successor.phone
                # Delete the successor from the right subtree
                node.right, _ = self._delete_recursive(node.right, successor.name)
                return node, True

    def _find_min(self, node):
        """Find the node with minimum value (leftmost node)."""
        current = node
        while current.left is not None:
            current = current.left
        return current

    def display_contacts(self):
        """
        Display all contacts alphabetically using inorder traversal.
        Returns list of (name, phone) tuples.
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        """Recursively perform inorder traversal (produces alphabetical order)."""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append((node.name, node.phone))
            self._inorder_recursive(node.right, result)

    def is_empty(self):
        """Check if the directory is empty."""
        return self.root is None


def print_menu():
    """Display the menu options."""
    print("\n===== Contact Directory =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display All Contacts")
    print("5. Exit")


def main():
    """
    Menu-driven interface for the Contact Directory application.
    Provides a simple CLI for managing contacts.
    """
    directory = ContactDirectory()

    # Add some example contacts for demonstration
    print("Adding example contacts...")
    directory.add_contact("Sohan", "9123456789")
    directory.add_contact("Rahul", "9876543210")
    directory.add_contact("Amit", "9876501234")
    print("Example contacts added: Sohan, Rahul, Amit")

    while True:
        print_menu()

        try:
            choice = input("\nEnter your choice: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if choice == "1":
            # Add Contact
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()

            if not name:
                print("Error: Name cannot be empty.")
                continue

            if not phone:
                print("Error: Phone number cannot be empty.")
                continue

            success = directory.add_contact(name, phone)
            if success:
                print("Contact added successfully.")
            else:
                print(f"Contact '{name}' already exists. Phone number updated.")

        elif choice == "2":
            # Search Contact
            name = input("Search name: ").strip()

            if not name:
                print("Error: Name cannot be empty.")
                continue

            result = directory.search_contact(name)
            if result:
                print(f"Name: {result[0]}")
                print(f"Phone: {result[1]}")
            else:
                print("Contact not found.")

        elif choice == "3":
            # Delete Contact
            name = input("Delete name: ").strip()

            if not name:
                print("Error: Name cannot be empty.")
                continue

            if directory.is_empty():
                print("Directory is empty. Nothing to delete.")
                continue

            deleted = directory.delete_contact(name)
            if deleted:
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")

        elif choice == "4":
            # Display All Contacts
            if directory.is_empty():
                print("Directory is empty.")
            else:
                contacts = directory.display_contacts()
                print("\n--- All Contacts (Alphabetical) ---")
                for name, phone in contacts:
                    print(f"{name:10s} - {phone}")
                print(f"\nTotal contacts: {len(contacts)}")

        elif choice == "5":
            # Exit
            print("Goodbye!")
            break

        else:
            # Invalid menu choice
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()