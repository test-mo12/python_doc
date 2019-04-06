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

print(tuple1)       # (1,)
print(tuple2)       # (1, 2)
print(tuple3)       # (1, 2)
print(tuple4)       # (1, 2, 3, 4)
print(tuple5)       # (1, 2, 1, 2, 1, 2)
print(tuple6)       # (2, 4)
print(tuple5[1:3])  # (2, 1)

x, y = tuple3       # unpacking tuple

if 2 in tuple5:
    print("exists")
```

## 2.16 Swapping Variables

using tuple concept - _define a tuple and unpack it_

```python
x = 10
y = 11
x, y = y, x     # x, y = (y, x)
```

## 2.17 Arrays

behaves similar to lists, used for large number of data, perfomes faster and optimized

> ref: [Typecodes](https://docs.python.org/3/library/array.html)

`array(typecode, list)`

```python
from array import array
numbers = array('i', [1, 2, 3])
```

## 2.18 Sets

a collection with no duplicates

- does not support indexing
- unordered not in sequence

```python
numbers = [1, 12, 2, 1, 4, 12, 2, 2, 1, 4, 6]
a = {1, 7, 4, 9}
uniques = set(numbers)
uniques.add(10)
uniques.remove(4)

print(uniques)          # {1, 2, 6, 10, 12}
print(len(uniques))     # 5

# union (all from uniques and a)
print(uniques | a)          # {1, 2, 6, 7, 9, 10, 12}

# intersect (just ones in both uniques and a)
print(uniques & a)          # {1, 12}

# difference (in uniques but not in a)
print(uniques - a)          # {2, 10, 6}

# symatric difference (either in uniques or in a, not in both)
print(uniques ^ a)          # {2, 6, 7, 9, 10}

if 12 in uniques & a:
    print("12 in both")
```

## 2.19 Dictionaries

collection of key, value pairs

```python
point1 = {'x': 1, 'y': 2}
point2 = dict(x=3, y=4)

print(point1)                   # {'x': 1, 'y': 2}
print(point2)                   # {'x': 3, 'y': 4}
print(point1['x'])              # 1
point1['z'] = 6
print(point1)                   # {'x': 1, 'y': 2, 'z': 6}
print(point1['a'])              # -> KeyError

if 'a' in point1:
    print(point1['a'])
# OR
print(point1.get('a'))          # None
print(point1.get('a', 0))       # 0 -> default value, if the key not exists

del point1['x']
print(point1)                   # {'y': 2, 'z': 6}

for key in point1:
    print(key, point1[key])     # y 2  z 6

for x in point1.items():
    print(x)                    # ('y', 2) ('z', 6)

for key, value in point1.items():
    print(key, value)           # y 2  z 6
```

## 2.20 Dictionary Comprehensions

```python
values1 = [x**2 for x in range(5)]
values2 = {x**2 for x in range(5)}
values3 = {x: x**2 for x in range(5)}

print(values1)      # [0, 1, 4, 9, 16] -> list
print(values2)      # {0, 1, 4, 9, 16} -> set
print(values3)      # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16} -> dictionary
```

## 2.21 Generators

iterable object, used for big amount of values, in each step it generates the next value instead of generating all of them and storing in memory

```python
from sys import getsizeof
listValues = [x**2 for x in range(50000)]
generatorValues = (x**2 for x in range(50000))

print("list:", getsizeof(listValues))               # list: 406496
print("generator:", getsizeof(generatorValues))     # generator: 120
```

## 2.22 Unpacking Operator `*`

```python
numbers = [1, 2, 4]
print(numbers)              # [1, 2, 4]
print(*numbers)             # 1 2 4

values1 = [*range(6), *"hello"]
print(values1)              # [0, 1, 2, 3, 4, 5, 'h', 'e', 'l', 'l', 'o']

first_list = [1, 2, 3]
second_list = [3, 4]
values2 = [*first_list, *"a", *second_list]
print(values2)              # [1, 2, 3, 'a', 3, 4]

first_dict = {'x': 3, 'y': 4}
second_dict = {'x': 23, 'z': 7}
values3 = {**first_dict, **second_dict, 'p': 43}
print(values3)              # {'x': 23, 'y': 4, 'z': 7, 'p': 43}
```

## Exercise

- [Most Frequent Character](../files/py/most_frequent_char.py)
