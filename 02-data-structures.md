## 2. Data Structures

### 2.1 Lists

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

### 2.2 List Operations

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

### 2.3 Lists Unpacking

## Python Builtin Functions

> ref: [python 3 builtin functions](https://docs.python.org/3/library/functions.html)

`print()`:

- prints it's argument out to the terminal

- puts `\n` (new line) at the end of output string, unless `end = ""` is declared

- takes different arguments: `string`, `int`, `float`, `boolean`, `list`, `tuple`, `dictionary` etc...

```python
print("some text")
print("some text", end=" ")
print('*' * 4) # prints 4 *
print(4)
```

`len()`: gives the length of any object

```python
len("some string")
len([1, 4, 5])
```

`round()`, `abs()`

```python
PI = 3.14
print(round(PI))    # rounds the number -> 3
print(abs(PI))      # absolute value
```

`range([start,] stop[, step])`: gives a sequence of numbers

```python
for i in range(9):
    print(i, end=' ')       # 0 1 2 3 4 5 6 7 8
print('...')
for i in range(2, 9):
    print(i, end=' ')       # 2 3 4 5 6 7 8
print('...')
for i in range(1, 9, 2):
    print(i, end=' ')       # 1 3 5 7
print('...')
```
