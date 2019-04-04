# 3. Exceptions

## 3.1 try block

```python
try:
    pass
except (Exception1, Exception2, ...):
    pass
else:
    pass
finally:
    pass
```

example:

```python
try:
    age = int(input("age: "))
    xfactor = 10 / age
except ValueError as ex:
    print("age must be an integer")
    print(ex)
    print(type(ex))
except ZeroDivisionError:
    print("age can not be 0.")
else:
    print("no exceptions were thrown")
print("execution continues...")

try:
    age = int(input("age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("enter a valid number for age")
else:
    print("no exceptions were thrown")
finally:
    print("this block will be executed in both cases, if an exception is thrown or not3")
```

## 3.2 `with` Statement

with statement manages automatically to open a file and close it at the end

all the objects which have `__enter__` and `__exit__` magic methods can be used with `with`

```python
try:
    with open("app.py") as file, open("otherfile.txt") as otherfile:
        print("file will be opened and closed automatically...")
except (NameError, FileNotFoundError):
    print("file could not be opened")
else:
    print("no exceptions were thrown")
```

## 3.3 Raising Exceptions

> ref: [Python 3 Builtin Exceptions](https://docs.python.org/3/library/exceptions.html)

```python
def calc_xfactor(age):
    if not age > 0:
        raise ValueError("age can not be less than 0")
    return 10 / age

try:
    calc_xfactor(-1)
except ValueError as error:
    print(error)
```

## 3.4 Cost of Raising Exception

Raising Exceptions costs time, so it should be used if is needed

> with `timeit`, time for execution a piece of code for several times could be measured

```python
from timeit import timeit

code1 = """
def calc_xfactor(age):
    if not age > 0:
        raise ValueError("age can not be less than 0")
    return 10 / age

try:
    calc_xfactor(-1)
except ValueError as error:
    pass
"""

code2 = """
def calc_xfactor(age):
    if not age > 0:
        return None
    return 10 / age

xfactor = calc_xfactor(-1)
if xfactor == None:
    pass
"""

print("code1: ", timeit(code1, number=10000))   # code1:  0.004462296000000001
print("code2: ", timeit(code2, number=10000))   # code2:  0.0015537750000000003
```
