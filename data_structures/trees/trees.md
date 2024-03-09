# Trees

A tree is a non-linear data structure and a hierarchy consisting of a collection of nodes
such that each node of the tree stores a value and a list of references to the other nodes (the "children").


## Binary Tree
A binary tree is a DS composed of nodes, each has at most, two children, referred to as left and right nodes.
The tree starts off with a single node know as the root. 
Each node contains the following:
- Data
- Pointer to the left child
- Pointer to the right child
- When leaf node, pointers left and right point to null.


### Types of binary trees

- Full Binary Tree
  - A full BT is a special type of binary tree in which every parent node/internal node has either two or no children.

- Perfect binary Tree
  - A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

- Complete BT
  - A complete BT is a BT in which all the levels are completely filled except possible the lowest one, which is filled from the left. 



## Binary Search Tree
A BST isa BT where each node contains a key and an optional associated value.
It allows particular fast lookup, addition, and removal of items. 

- The left subtree of a particular node will always contain nodes with keys less than node's key
- The right subtree of a particular node will always contain nodes with keys greater than node's key.
- The left and the right subtree of a particular node will also, in turn, be binary search trees.

### Time Complexity





## Space Complexity
- Worst case O(n)


### Static Arrays:
- Size or number of elements in static array is fixed
- Arrays content can be modified, but the memory space allocated to it remains constant.

### Dynamic Arrays
- Size or number of elements in a dynamic arrays can change.
- Dynamic arrays allow elements to be added and removed at the run time.


### Good at:
- Fast lookups
- Fast push/pop
- Ordered

### Bad at:
- Slow inserts
- Slow deletes
- Fixed size (using static array)

