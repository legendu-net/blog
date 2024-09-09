Status: published
Date: 2023-05-20 11:57:13
Modified: 2023-06-10 18:03:30
Author: Benjamin Du
Slug: tree-based-data-structures
Title: Tree-Based Data Structures
Category: Computer Science
Tags: Computer Science, programming

**Things on this page are fragmentary and immature notes/thoughts of the author. Please read with your own judgement!**

## BST vs AVL Tree vs Red-black Tree

1. BST is not necessarily balanced and has a worst lookup time of O(n).
2. AVL tree is strictly balanced BST.
3. Red-black is between BST and AVL tree.
    It is sort of balanced but not strictly balanced.
    A red-black tree is faster for insertion/deletion compared to an AVL tree
    as it requires less operations for rotation to keep the tree (sort of) balanced.
    However, it is slightly slower for lookup compared to an AVL tree.
    Red-black trees are more generally useful instead of for binary search only.

## Binary Tree vs B-Tree

1. B-Trees are self-balancing.
2. B-trees are designed to handle large amounts of data efficiently, 
    particularly in scenarios 
    where the data is stored on disk or in other secondary storage devices.
    For example, 
    B-Trees are typically used for database indexing.

## B-Tree vs Red-black Tree

B-trees and red-black trees are both self-balancing binary search trees that provide efficient operations for insertion, deletion, and search. However, they have different characteristics and are suited for different use cases.


### B-trees:

B-trees are designed to handle large amounts of data efficiently, particularly in scenarios where the data is stored on disk or in other secondary storage devices.
They have a variable number of keys per node, typically denoted by the parameter "b," which determines the maximum number of children a node can have.
B-trees are optimized for minimizing disk I/O operations by maintaining a balanced tree structure, which allows for efficient sequential access.
They are commonly used in file systems and databases to efficiently store and retrieve data from disk.
B-trees provide logarithmic time complexity for search, insert, and delete operations, typically O(log n), where n is the number of elements in the tree.
B-trees have a higher branching factor compared to red-black trees, resulting in shallower trees and fewer levels.

### Red-black trees:

Red-black trees are balanced binary search trees that guarantee relatively uniform height, which ensures efficient operations even for in-memory data structures.
They maintain a set of additional properties that ensure the tree remains balanced, such as the coloring of nodes (either red or black) and rotation operations.
Red-black trees are commonly used in programming language libraries and other in-memory data structures where the data size is not extremely large.
They provide efficient worst-case time complexity for search, insert, and delete operations, all with a time complexity of O(log n), where n is the number of elements in the tree.
Red-black trees have a higher overhead in terms of memory usage compared to B-trees due to the additional properties and color information stored in each node.

In summary, 
B-trees are optimized for disk-based storage systems, 
while red-black trees are primarily used for in-memory data structures. 
B-trees excel in scenarios where the data size is significant and efficient disk I/O is crucial. 
Red-black trees are suitable for applications where the data size is manageable and balanced operations are required.

## Heap

1. (Binary) heap is nearly compelete binary tree.
2. A max heap requires each parent to be greater or equal to its children, 
    and a min heap requires each parent to be less or equal to its children.
3. Max heap is useful for heapsort while min heap is useful for priority queue.
4. A heap is typically implemented using an array.
    - 1-based index
    - node $i$'s left child is node $2i$
    - node $i$'s right child is node $2i+1$

## References

- [Heaps in 3 minutes — Intro](https://www.youtube.com/watch?v=0wPlzMU-k00)

- [Trees Compared and Visualized | BST vs AVL vs Red-Black vs Splay vs Heap | Geekific](https://www.youtube.com/watch?v=hmSFuM2Tglw)

- [Data Structure Visualizations](https://www.cs.usfca.edu/~galles/visualization/Algorithms.html)
