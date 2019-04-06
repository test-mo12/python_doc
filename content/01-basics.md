# 1. Basics

## 1.1 Variables

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

## 1.2 Strings

escape characters: `\'`, `\"`, `\\`, `\n`

formatted strings

```python
first = 'John'
last = 'Smith'
print(f"Hi I am {first} {last}") # any valid statement can go between {}
```

### String Methods

```python
course = " Python programming course"
print(course.upper())
print(course.lower())
print(course.title())           # make every first character Capital
print(course.strip())           # trimming white space around the string
print(course.find("Pro"))       # to find index of the beginning of a substring (Case Sensitive)
print(course.replace("P", "C")) # to replace a substing
print("Programming" in course)  # to check whether a substring exists in this string
print(course.startswith('P')    # checks whether the string starts with a substring
```

## 1.3 Numbers

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

## 1.4 Arithmetic Operators

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

## 1.5 Math Module

> ref: [python 3 math module](https://docs.python.org/3/library/math.html)

```python
import math
PI = 3.14
print(math.floor(PI))
```

## 1.6 Type Conversion

```python
x = input("x: ")  # x -> string
y = int(x)
y = float(x)
y = bool(x)
y = str(x)
```

## 1.7 Falsy Values

Any value other than these is treated as `True`

**`False`:**

- `""` _empty string_
- `0` _zero_
- `[]` _empty list_
- `None` _None value_

## 1.8 Comparison Operators

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

## 1.9 Logical Operators

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

> **`pass` Keyword** is a place holder, whenever is needed to have a block without codes inside, pass keyword can be used to show this block does nothing and is empty. _without pass an error will be raised for an empty block of code_

## 1.10 Conditional Statements

### 1.10.1 `if...elif...else`

```python
if condition1:
    pass
elif condition2:
    pass
else:
    pass
```

example:

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

### 1.10.2 Ternary Operator

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

## statement above is completely equivalent to this if statement below

if not name.strip():
    result = "Empty String"
else:
    result = f"your name is {name.strip()}"
```

## 1.11 Loops

### 1.11.1 `for...else...`

to iterate over an iterable object like strings, lists, sequence of numbers etc...

```python
for item in iterableitems:
    pass
else:
    pass
```

example:

```python
for c in "Python":
    print(c, end=" ")       # output -> P y t h o n
print('...')
for x in [12, 4, -4]:
    print(x, end=" ")       # output -> 12 4 -4
print('...')
for i in range(1, 9, 2):    # output -> 1 3 5 7
    print(i, end=" ")
print('...')


names = ['johen', 'mary']
for name in names:
    if name.startswith('j'):
        print('found')
        break
else:
    print('not found')
```

#### 1.11.2 `while...else...`

```python
while condition:
    pass
else:
    pass
```

example:

```python
guess = 0
answer = 5
count = 0
max_guess = 3
while count < max_guess:
    guess = int(input("Guess > "))
    count += 1
    if guess == answer:
        print("you won")
        break
else:
    print('you gave 3 false guesses -> game over!')
```

### 1.12 Functions

```python
def function_name(parameters):
    pass
    # return value
```

#### Parameter Type Annotation

has no influence of parameter types, used just to show which types should be used for that parameter

`def func(param1: int, param2: str) -> int`

> last `int` after arrow shows the type of return value

#### Parameters

default values can be defined for parameters so if no arguments is given in function call, default values will be used `def func(arg=10)`

#### return

by default, if there is no return statement in a function, python returns `None` as the return value for that function

#### Arguments

arguments have different forms:

- positional arguments: `func(arg1, arg2, arg3)` the order of given arguments **matters**

- keyword arguments: `func(arg2=2, arg3=5, arg1=10)` the order of given arguments **doesn't matter**

##### Order of Arguments

1. positional arguments
2. keyword arguments

```python
# Function Definition
def increment(number, by):
    return number + by

# Call the Function
print(increment(3, 4))
```

#### Multiple Arguments

```python
def multiply(*params):
    total = 1
    for number in params:
        total *= number
    return total

print(multiply(2, 3, 4, 5))
```

> by passing `*params` _with asterisk_ in function definition and multiple arguments in function call, python treats them as a `tuple` (immutable or readonly list)

#### Multiple Keyword Arguments

```python
def save_user(**user):
    print(user)
    # print(user["id"])
    # print(user["name"])

print(save_user(id=3, name='John'))  # {'id: 3, 'name': 'John'}
```

> by passing `**params` _with double asterisk_ in function definition and multiple keyword arguments in function call, python treats them as a `dictionary` (set of key value pairs)

### 1.13 Scopes

- local: function scope _inside a funntion_
- global: file scope _anywhere in the file_

local variables have higher priority, so if two variables with the same name are defined, one in global scope and the other in function scope, working in that functions means the other variable inside the function and it will not use the global one. To say ecplicitely to use the global variable it should be written with `global` keyword, so python knows in this function the global one is used

```python
message = "hello"

def greet():
    global message
    print(message)

greet()
```

> **BAD PRACTICE**: Using global variables

\>>> [FizzBuzz Exercise](../playground/fizz_buzz.py)
