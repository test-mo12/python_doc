# 2. Data Structures

## 2.1 Lists

a mutable iterable sequense of data

```python
names = ['John', 'Mary', 'David']
ones = [1] * 3
matrix = [[0, 1], [2, 3]]
combined = names + ones
numbers = list(range(10))
chars = list("hello world!")
print(combined)     # ['John', 'Mary', 'David', 1, 1, 1]
print(matrix)       # [[0, 1], [2, 3]]
print(numbers)      # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(chars)        # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', '!']
print(len(numbers)) # 10
```

## 2.2 List Operations

- list items or elements can be accessed by their indices

- \+ indices starts from 0 (beginning of list)

- \- indices starts from -1 (end of list)

```python
letters = ["a", "b", "c", "d", "e", "f", "g"]
letters[2] = "C"
print(letters[0])       # a
print(letters[-1])      # g
print(letters[:])       # ['a', 'b', 'C', 'd', 'e', 'f', 'g']
print(letters[2:])      # ['C', 'd', 'e', 'f', 'g']
print(letters[:4])      # ['a', 'b', 'C', 'd']
print(letters[1:3])     # ['b', 'C']
print(letters[1::2])    # ['b', 'd', 'f']
print(letters[::-1])    # ['g', 'f', 'e', 'd', 'C', 'b', 'a']
print(letters[:-2:3])   # ['a', 'd']
```

## 2.3 Lists Unpacking

```python
numbers = [1, 3, 6, 7, 8]
x, y, z, a, b = numbers     # number of variables and list items should match
x, y, *other = numbers      # packing and unpacking
first, *other, last = numbers      # packing and unpacking
```

## 2.4 Looping over Lists

to get just the value of an item

```python
letters = ['a', 'b', 'c']
for letter in letters:
    print(letter)
```

to get the value and index of an item

```python
letters = ['a', 'b', 'c']
for letter in enumerate(letters):
    print(letter[0])        # index
    print(letter[1])        # value

# using unpacking method
for index, letter in enumerate(letters):
    print(index, letter)
```

> `enumerate()` returns a tuple of index and item -> (index, item)

## 2.5 Adding or Removing items

Methods:

- `.append()`: add an item at the end of list

- `.insert()`: add an item in given position

- `.pop()`: removes the last item of the list

  - to remove an item at given index, the index should be passed to this method

- `.remove()`: finds the first occurance of a value in list and removes it

- `del` keyword: deletes a subset of items using their indices in list, could be just one item or more

- `.clear()`: removes all the object in the list

```python
letters = ['a', 'b', 'c', 'f', 'p', 'r', '3', 2]
# Add
letters.append('d')
letters.insert(0, '-')
# Remove
letters.pop()
letters.pop(1)
letters.remove('c')
del letters[0]
del letters[0:2]
letters.clear()
```

## 2.6 Finding Items

Methods:

- `.index()`: finds index of an item, if not finds one returns a `ValueError`

  - to check the existence of an item in the list use `in` operator

- `.count()`: returns the number of occurrences of an item in the list

```python
letters = ['a', 'b', 'c', 'f', 'p', 'r', '3', 2]
if 'o' in letters:
    print(letters.index('o'))

print(letters.count('a'))
```

## 2.7 Sorting Lists

- `.sort()`: sorts a list in ascending order
  - to sort in descending order just pass the `reverse=True` argument
  - `.sort()` will modify the original list. to have a sorted copy of a list use builtin function `sorted()`

```python
numbers = [2, 3, 6, 12, 76, -15]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)
```

## 2.8 Lambda Functions

a simple one line anynomus function that we can pass to other functions

`lambda parameters:expressen`

```python
items = [
    ("product1", 32),
    ("product2", 8),
    ("product3", 14)
]

items.sort(key=lambda item: item[1])    # sort based on second item in tuple
print(items)                            # [('product2', 8), ('product3', 14), ('product1', 32)]
```

## 2.9 Map Function

to transform an iterable object or extract some part of it

```python
items = [
    ("product1", 32),
    ("product2", 8),
    ("product3", 14)
]

prices = list(map(lambda item: item[1], items))
print(prices)       # [32, 8, 14]
```

## 2.10 Filter Function

to extract some items out of an object with a filter

```python
items = [
    ("product1", 32),
    ("product2", 8),
    ("product3", 14)
]

filtered_items = list(filter(lambda item: item[1] >= 10, items))
print(filtered_items)       # [('product1', 32), ('product3', 14)]
```

## 2.11 List Comprehensions (alternative for map and filter)

`[expression for item in items]`

```python
items = [
    ("product1", 32),
    ("product2", 8),
    ("product3", 14)
]

# filtered_items = list(filter(lambda item: item[1] >= 10, items))
filtered_items = [item for item in items if item[1] >= 10]
print(filtered_items)       # [('product1', 32), ('product3', 14)]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)               # [32, 8, 14]
```

## 2.12 Zip Function

```python
list1 = [1, 2, 3]
list2 = [10, 20, 30]

combined_list = list(zip("abc", list1, list2))
print(combined_list)        # [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
```

## 2.13 Stacks

LIFO: Last In - First Out

a list can be treated as a stack

- `.append()` add item to top of stack

- `.pop()` remove item from top of stack

- `var[-1]` get item from top of stack using -1 index

```python
x = []
x.append(1)
x.append(2)
x.append(3)
x.pop()
if x:               # if x is not an empty list
    print(x[-1])    # 2
```

## 2.14 Queues

FIFO: First In - First Out

```python
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)        # deque([1, 2, 3])
queue.popleft()     # removes an item from ends of the list
print(queue)        # deque([2, 3])
if not queue:
    print("empty")
```

## 2.15 Tuple

a readonly list - can not be modified

```python
tuple1 = 1,
tuple2 = 1, 2
tuple3 = (1, 2)
tuple4 = (1, 2) + (3, 4)
tuple5 = (1, 2) * 3
tuple6 = tuple([2, 4])

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)
print(tuple6)

print(tuple5[1:3])

x, y = tuple3       # unpacking tuple

```
