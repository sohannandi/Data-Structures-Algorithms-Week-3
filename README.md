# Week 3: Data Structures & Algorithms

This repository contains implementations for Week 3 of the Data Structures & Algorithms course, focusing on Binary Search Trees, Tree Traversals, Hash Maps, and Collision Handling.

## Table of Contents
- [Week 3 Overview](#week-3-overview)
- [Assignments](#assignments)
  - [Assignment 1: BST Search](#assignment-1-bst-search)
  - [Assignment 2: Recursive Tree Traversals](#assignment-2-recursive-tree-traversals)
  - [Assignment 3: Array-Based HashMap](#assignment-3-array-based-hashmap)
  - [Assignment 4: Hash Table with Linear Probing](#assignment-4-hash-table-with-linear-probing)
- [Mini Project: Contact Directory](#mini-project-contact-directory)
- [Practice Set](#practice-set)
- [Technologies Used](#technologies-used)
- [How to Run Programs](#how-to-run-programs)
- [Sample Inputs and Outputs](#sample-inputs-and-outputs)
- [Key Data Structures and Algorithms](#key-data-structures-and-algorithms)

## Week 3 Overview

Week 3 focuses on implementing fundamental data structures:
1. Binary Search Trees (BST) with insertion and search
2. Three recursive tree traversals (inorder, preorder, postorder)
3. HashMap using array-based storage
4. Hash table collision handling using Linear Probing
5. Mini project: Contact Directory using BST

## Assignments

### Assignment 1: BST Search
**File:** `assignment-1-bst-search/bst_search.py`

Implements a Binary Search Tree that supports:
- Insertion of values following BST ordering rules
- Search for a specified value
- Duplicate value handling (ignored)

**Key Features:**
- Node-based BST implementation
- Recursive insert and search methods
- Clear handling of duplicates (not stored)

### Assignment 2: Recursive Tree Traversals
**File:** `assignment-2-tree-traversals/tree_traversals.py`

Implements the three standard recursive binary-tree traversals:
- Inorder (Left, Root, Right)
- Preorder (Root, Left, Right)
- Postorder (Left, Right, Root)

**Key Features:**
- All traversals implemented recursively
- Tested with example tree from PRD
- Handles empty tree case

### Assignment 3: Array-Based HashMap
**File:** `assignment-3-hashmap/hashmap.py`

Implements a basic HashMap using array-based storage with:
- Fixed-size array/table
- Hash function: `hash(key) = key % size`
- Separate chaining for collision handling
- `put(key, value)` and `get(key)` operations

**Key Features:**
- Array-based storage using list of buckets
- Modulo-based hash function
- Collision handling via separate chaining
- Proper handling of missing keys (returns None)

### Assignment 4: Hash Table with Linear Probing
**File:** `assignment-4-linear-probing/linear_probing.py`

Implements collision handling in a hash table using Linear Probing:
- Fixed-size hash table
- Hash function: `hash(key) = key % size`
- Linear probing collision resolution
- Insert, search, delete, and display operations

**Key Features:**
- Linear probing for collision resolution
- Proper handling of table wrap-around
- Deletion using tombstone markers
- Full table condition handling

## Mini Project: Contact Directory
**File:** `mini-project-contact-directory/contact_directory.py`

Builds a Contact Directory using a Binary Search Tree organized by contact name.

**Features:**
- Add Contact (name, phone number)
- Search Contact by name
- Delete Contact by name (handles all three BST deletion cases)
- Display All Contacts alphabetically (inorder traversal)
- Menu-driven interface
- Duplicate name handling (updates phone number)

**Contact Data Structure:**
```python
ContactNode:
    name (string) - BST key
    phone (string) - contact phone number
    left, right (ContactNode) - BST children
```

## Practice Set

### Practice 1: Recursion
**File:** `practice/factorial_fibonacci.py`
- Recursive factorial implementation
- Recursive Fibonacci implementation

### Practice 2: BST Operations
**File:** `practice/bst_min_max.py`
- Finding minimum value in BST (leftmost node)
- Finding maximum value in BST (rightmost node)

### Practice 3: Tree Traversals
Covered in Assignment 2

### Practice 4: BST Minimum and Maximum
**File:** `practice/bst_min_max.py`

### Practice 5: Recursive Array Sum
**File:** `practice/recursive_array_sum.py`
- Recursive function to sum array elements
- Two implementations: index-based and slice-based

## Technologies Used

- **Language:** Python 3.x
- **Data Structures:** 
  - Binary Search Trees (node-based)
  - Arrays (for HashMap and hash table)
  - Linked lists conceptually (separate chaining in HashMap)
- **Algorithms:**
  - BST insertion and search
  - Recursive tree traversals
  - Hash functions (modulo)
  - Collision resolution (separate chaining, linear probing)
  - Recursive algorithms (factorial, fibonacci, array sum)

## How to Run Programs

Each assignment and practice file can be run independently using Python:

```bash
# Assignment 1: BST Search
python week-3/assignment-1-bst-search/bst_search.py

# Assignment 2: Tree Traversals
python week-3/assignment-2-tree-traversals/tree_traversals.py

# Assignment 3: HashMap
python week-3/assignment-3-hashmap/hashmap.py

# Assignment 4: Linear Probing
python week-3/assignment-4-linear-probing/linear_probing.py

# Mini Project: Contact Directory
python week-3/mini-project-contact-directory/contact_directory.py

# Practice Files
python week-3/practice/factorial_fibonacci.py
python week-3/practice/bst_min_max.py
python week-3/practice/recursive_array_sum.py
```

## Sample Inputs and Outputs

### Assignment 1: BST Search
**Input:**
```
Insert: 50, 30, 70, 20, 40, 60, 80
Search: 40
```
**Output:**
```
40 found
```

**Input:**
```
Search: 90
```
**Output:**
```
90 not found
```

### Assignment 2: Tree Traversals
**Example Tree:**
```
        50
       /  \
     30    70
    / \    / \
   20 40  60 80
```
**Output:**
```
Inorder:   20 30 40 50 60 70 80
Preorder:  50 30 20 40 70 60 80
Postorder: 20 40 30 60 80 70 50
```

### Assignment 3: HashMap
**Input:**
```
put(25, "Sohan")
get(25)
```
**Output:**
```
Sohan
```

### Assignment 4: Linear Probing
**Input:**
```
Table size = 10
hash(key) = key % 10
Insert: 25, 35
```
**Output:**
```
25 → index 5
35 → index 6 (collision resolved via linear probing)
```

### Mini Project: Contact Directory
**Menu:**
```
===== Contact Directory =====
1. Add Contact
2. Search Contact
3. Delete Contact
4. Display All Contacts
5. Exit
Enter your choice:
```

**Sample Session:**
```
Add Contact
Name: Sohan
Phone: 9123456789
Contact added successfully.

Search: Sohan
Name: Sohan
Phone: 9123456789

Display All Contacts:
Saikat   - 9876501234
Rahul  - 9876543210
Sohan  - 9123456789
```

## Key Data Structures and Algorithms

### Binary Search Tree (BST)
- **Property:** Left subtree < Node < Right subtree
- **Operations:** Insertion (O(h)), Search (O(h)), Deletion (O(h))
- **Traversals:** Inorder (sorted), Preorder, Postorder (all O(n))

### HashMap / Hash Table
- **Hash Function:** Maps keys to array indices
- **Collision Handling:**
  - Separate Chaining (Assignment 3): Each bucket stores linked list of key-value pairs
  - Linear Probing (Assignment 4): Probe sequentially for next available slot
- **Operations:** Insert (O(1) avg), Search (O(1) avg), Delete (O(1) avg)

### Recursion
- **Principle:** Function calls itself with smaller subproblems
- **Base Case:** Condition to stop recursion
- **Examples:** Factorial, Fibonacci, Tree Traversals, Array Sum

### BST Properties Utilized
- **Minimum Value:** Leftmost node in the tree
- **Maximum Value:** Rightmost node in the tree
- **Inorder Traversal:** Produces elements in sorted ascending order

## Learning Outcomes

After completing Week 3, students should understand:
1. How Binary Search Trees work and maintain ordering property
2. How BST search and insertion operate using comparisons
3. Why inorder traversal of BST produces sorted output
4. How recursive tree traversal works via divide-and-conquer
5. How hash functions map keys to table indexes
6. What hash collisions are and why they occur
7. How Linear Probing resolves collisions by probing sequentially
8. How data structures can be combined to build practical applications (Contact Directory)
9. How to handle edge cases like empty structures, duplicates, and full tables
10. The importance of clear code organization and modular design

---
*Week 3 implementation complete. All assignments, mini-project, and practice exercises implemented as per PRD specifications.*
