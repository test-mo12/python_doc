# Python_doc

## 1. Basics

### 1.1 Variables

Naming Convention

- lowercase with underscore in between
- there is no constants in python, but to show a variable is constant and should not be changed, use uppercase

Variable Types

- are determined _dynamically_ by python, no need to set types of variables while declaring

Strings

- could be written within `' '`, `" "` or `""" """`
- they are sequences of characters behind the scenes, so could be treated as `list`
- to use `'` inside of string use double `"` and vice versa and to write multiple strings, `"""` should be used

```python
students_count = 1000             # int
rating = 9.4555                   # float
x, y = 10, 4                      # multi assignment in one line
a = b = 9                         # assign one value to multiple variables
is_published = True               # (False) boolean
course_name = 'Python'            # string
course_title = "Python's course"  # string
course_description = """
some multiline
description text
"""
type(students_count)              # gets the type of a variable
age: int = 28                     # type annotation is a way to show type of variable while declaring but has no serious effects, which means this variable could be assigned with another type of value
age = 'some string'               # gives no error
id(age)                           # to get the address of memory location where this variable is stored
```

> all these variables above are _immutable_, which means the value of those could not be changed in that refrence, so when they're changed python will automatically allocate a new memory location and refrence that variable to the new refrence. but _lists_ are mutable so when the value of an element in them is changed, it will be affected in that place(reference)

### 1.2 Strings

escape characters: `\'`, `\"`, `\\`, `\n`

formatted strings

```python
first = 'John'
last = 'Smith'
print(f"Hi I am {first} {last}") # any valid statement can go between {}
```

#### String Methods

```python
course = " Python programming course"
print(course.upper())
print(course.lower())
print(course.title())           # make every first character Capital
print(course.strip())           # trimming white space around the string
print(course.find("Pro"))       # to find index of the beginning of a substring (Case Sensitive)
print(course.replace("P", "C")) # to replace a substing
print("Programming" in course)  # to check whether a substring exists in this string
```

### 1.3 Numbers

```python
x = 10          # decimal
b = 0b10        # binary -> 2
print(b)        # prints decimal format
print(bin(b))   # prints binary format
h = 0x12c       # hexadecimal -> 300
print(h)        # prints decimal format
print(hex(h))   # prints hexadecimal format
c = 1 + 2j      # complex number -> 1 + 2i
print(c)        # prints complex format
```

### 1.4 Arithmetic Operators

```python
x = 10 + 3
x = 10 - 3
x = 10 * 3
x = 10 / 3      # -> 3.333333
x = 10 // 3     # -> 3
x = 10 % 3      # -> 1 (remainder of devision)
x = 10 ** 3     # -> 1000 (exponent)

x += 10         # -> x = x + 10
x -= 10         # -> x = x - 10
x *= 10         # -> x = x * 10
x /= 10         # -> x = x / 10
```

### 1.5 Math Module

> ref: [python 3 math module](https://docs.python.org/3/library/math.html)

```python
import math
PI = 3.14
print(math.floor(PI))
```

### 1.6 Type Conversion

```python
x = input("x: ")  # x -> string
y = int(x)
y = float(x)
y = bool(x)
y = str(x)
```

### 1.7 Falsy Values

Any value other than these is treated as `True`

**`False`:**

- `""` _empty string_
- `0` _zero_
- `[]` _empty list_
- `None` _None value_

### 1.8 Comparison Operators

```python
a = 8
b = 10
c = 12
print(a > b)        # greater than
print(a >= b)       # greater than or equal
print(a < b)        # less than
print(a <= b)       # less than or equal
print(a == b)       # equal
print(a != b)       # not equal
print(a <= b < b )  # chaining comparison operators like real math
```

### 1.9 Logical Operators

```python
a = True
b = False
if a and b:
    print("AND")
elif a or b:
    print("OR")
elif not a:
    print("NOT")
```

### 1.10 Conditional Statements

```python
age = 28
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")
print("finished")
```

#### `pass` Keyword

is a place holder, whenever is needed to have a block without codes inside, pass keyword can be used to show this block does nothing and is empty. _without pass an error will be raised for an empty block of code_

```python
a = True
if a:
    pass
else:
    print("something")
```

#### Ternary Operator

very useful form of short if else statements

```python
x = a if condition else b
```

equivalent to this:

```python
if condition:
    x = a
else:
    x = b
```

example:

```python
name = " " # a string with a whitespace inside is not an empty string, to avoid whitespaces around, use strip()

result = "Empty String" if not name.strip() else f"your name is {name.strip()}"

### statement above is completely equivalent to this if statement below

if not name.strip():
    result = "Empty String"
else:
    result = f"your name is {name.strip()}"
```

### 1.11 For Loops

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

## Hints

> - python is case sensitive language `True` and `true` are not the same
