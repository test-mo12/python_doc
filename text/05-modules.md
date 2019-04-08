# 5. Modules

## 5.1 Making Modules

if the module is in the same directory as app.py

`calc.py`

```python
def calc_tax():
    print("calculating taxes")

def calc_price():
    print("calculating prices")
```

`app.py`

```python
from calc import calc_tax, calc_price

calc_price()
calc_tax()
```

## 5.2 Module Search Path

when a module is importe in a file python searches first in the same directory, if not found then in the next address in search path

```python
import sys

print(sys.path)
```

## 5.3 Packages

in python package means a directory with some modules inside, which has a `__init__.py`

`ecommerce/calc.py`

```python
def calc_tax():
    print("calculating taxes")

def calc_price():
    print("calculating prices")
```

`app.py`

```python
from ecommerce import calc

calc.calc_tax()
calc.calc_price()
```

> sub-packages could be created with the concept above

## 5.4 Package Info

`dir(module_name)` gets all methods inside the module

```python
print(calc.__name__)        # ecommerce.calc
print(calc.__package__)     # ecommerce
print(calc.__file__)        # "file path"
print(calc.__name__)        # ecommerce.calc
print(dir(calc))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'calc_price', 'calc_tax']
```

