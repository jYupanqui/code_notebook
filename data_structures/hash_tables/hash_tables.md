# Hash Tables

A hash table is a type of data structure that stores pairs of key-value. The key is sent to a hash function that
performs arithmetic operations on it. The result (commonly called the hash value or hashing) is the index
of the key-value pair in the hash table.

### Hash Function
A hash function takes a group of characters and maps it to a value of a certain length.
The hash value is representative of the original string of characters, but is normally smaller than the original.

Hashing is done for indexing and locating items in databases because it is easier to find the shorter hash value
than the longer string. Hashing is also used in encryption. This term is also known as a hashing
algorithm or message digest function.

### Collisions

A collision occurs when two keys get mapped to the same index. There are several ways of handling collisions:
- Linear Probing:
  - If a pair is hashed to a slot which is already occupied, it searches linearly for the next free slot in the table.
- Chaining:
  - The hash table will be an array of linked lists. All keys mapping to the same index will be stored as linked list nodes at that index.
- Resizing the hash table:
  - The size of the hash table can be increased in order to spread the hash entries further apart. A threshold value signifies the percentage of the hash table that needs to be occupied.


 

## Time Complexity 
| Syntax    | Average Case |
|-----------|--------------|
| Access    | O(1)         |
| Search    | O(1)         |
| Insertion | O(1)         |
| Deletion  | O(1)         |



## Space Complexity
- Worst case O(n)


### Good at:
- Fast lookups
- Fast inserts
- Flexible keys

### Bad at:
- Unordered (python dicts are ordered from 3.7)
- Slow key iteration

