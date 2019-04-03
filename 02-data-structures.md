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
