Status: published
Date: 2023-05-20 11:57:13
Modified: 2023-05-20 12:46:10
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
    Re-black trees are more generally useful instead of for binary search only.

## Binary Tree vs B-Tree

1. B-Trees are self-balancing.
2. B-Trees are for storing data on disk while binary tree are for storing data in memory.
3. B-Trees are typically used for database indexing.

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
