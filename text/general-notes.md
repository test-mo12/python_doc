# General Notes

## Python Builtin Functions

ref: [python 3 builtin functions](https://docs.python.org/3/library/functions.html)

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

`sorted()`: takes an iterable object and returns it sorted

- to reverse the sort _descinding_

```python
numbers = [2, 3, 6, 12, 76, -15]
x = sorted(numbers)
```

## Hints

- python is case sensitive language `True` and `true` are not the same

- String Prefixes:

    - f"string" : _formatted string
    
    - r"string"_: _raw string, no escape characters needed_