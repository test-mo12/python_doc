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
