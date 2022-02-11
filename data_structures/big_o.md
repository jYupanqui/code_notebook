#BIG O 
- how well a solution solves a problem
####Good code:
 - Scalable 
 - Readable


##BIG O'S 
- O(1) Constant - no loops

- O(log N) Logarithmic - usually searching algorithms have log n if they are sorted (Binary Search)

- O(n) Linear - for loops, while loops through n items

- O(n log(n)) Log Linear - usually sorting operations

- O(n^2) Quadratic - every element in a collection needs to be compared to ever other element. Two nested loops

- O(2^n) Exponential - recursive algorithms that solves a problem of size N

- O(n!) Factorial - you are adding a loop for every element

Iterating through half a collection is still O(n)

Two separate collections: O(a * b)

###WHAT CAN CAUSE TIME IN A FUNCTION?
- Operations (+,-, \*, /)
- Comparisons (<, >, ===)
- Looping (for, while)
- Outside Function call (function())

###RULE BOOK
- Rule 1: Always worst Case

- Rule 2: Remove Constants

- Rule 3: Different inputs should have different variables: O(a + b). A and B arrays nested would be: O(a * b), + for steps in order, * for nested steps

- Rule 4: Drop Non-dominant terms

###WHAT CAUSES SPACE COMPLEXITY?
- Variables
- Data Structures
- Function Call
- Allocations


###Exercises
1) The big o notation is O(3 + 4n) -> **O(n)**. Assuming the other function doesn't have any loops.
```
function funChallenge(input) {
  let a = 10; //O(1)
  a = 50 + 3; //O(1)

  for (let i = 0; i < input.length; i++) { //O(n)
    anotherFunction();//O(n)
    let stranger = true;//O(n)
    a++;//O(n)
  }
  return a; //O(1)
}
```


2) The big O notation is O(4 + 7 n) -> **O(n)**
```
function anotherFunChallenge(input) {
  let a = 5; // O(1)
  let b = 10;// O(1)
  let c = 50;// O(1)
  for (let i = 0; i < input; i++) { // O(n)
    let x = i + 1;// O(n)
    let y = i + 2;// O(n)
    let z = i + 3;// O(n)

  }
  for (let j = 0; j < input; j++) {// O(n)
    let p = j * 2;// O(n)
    let q = j * 2;// O(n)
  }
  let whoAmI = "I don't know";// O(1)
}
```


3) The big O is O(n^2)

```
# Log all pairs of array
box = ['a', 'b', 'c', 'd', 'e']

for i, item in enumerate(box):
    for j, item2 in enumerate(box):
        print(item, item2)


```