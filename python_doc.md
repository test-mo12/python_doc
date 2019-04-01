# python_doc

## 1. basics

### 1.1 variables

**naming convention**: lowercase with underscore in between

**variable types** are determined _dynamically_ by python, no need to set types of variables while declaring

**strings** could be write within `' '`, `" "` or `""" """`

> to use `'` inside of string use double `"` and vice versa and to write multiple strings, `"""` should be used

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

all these variables above are _immutable_, which means the value of those could not be changed in that refrence, so when they're changed python will automatically allocate a new memory location and refrence that variable to the new refrence. but _lists_ are mutable so when the value of an element in them is changed, it will be affected in that place(reference)

### 1.2 strings

---

## hints

> - python is case sensitive language `True` and `true` are not the same

---

## python builtin functions

`print()`:

- prints it's argument out to the terminal

- goes to new line after printing, unless `end = ''` is declared

- takes different arguments: `string`, `ìnt`, `float`, `boolean`, `list`, `tuple`, `dictionary` etc...

```python
print("some text")
print('*' * 4) # prints 4 *
print(4)
```

`len()`: gives the length of any object

```python
len("some string")
len([1, 4, 5])
```
