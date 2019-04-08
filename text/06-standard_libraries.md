# 6. Standard Libraries

## 6.1 Paths

> ref: [Python 3 pathlib Module](https://docs.python.org/3/library/pathlib.html)

```python
from pathlib import Path

print(Path(r"C:\Program Files\Microsoft"))      # C:\Program Files\Microsoft
print(Path("/usr/local/bin"))                   # /usr/local/bin
print(Path())                                   # .
print(Path("ecommerce/__init__.py"))            # ecommerce/__init__.py
print(Path() / "ecommerce" / "__init__.py")     # ecommerce/__init__.py
print(Path.home())                              # path of home directory

path = Path("ecommerce/__init__.py")
print(path.exists())                            # True
print(path.is_file())                           # True
print(path.is_dir())                            # False
print(path.name)                                # __init__.py
print(path.stem)                                # __init__
print(path.suffix)                              # .py
print(path.parent)                              # ecommerce
print(path.with_name("file.txt"))               # ecommerce/file.txt
print(path.with_suffix(".txt"))                 # ecommerce/__init__.txt
print(path.absolute())                          # absolute/full path of __init__.py
```

## 6.2 Directories

```python
from pathlib import Path

path = Path("ecommerce")

# checks whether directory exists
# path.exists()

# make this directory
# path.mkdir()

# renames the directory
# path.rename("ecommerce2")

# removes this directory
# path.rmdir()

# gets all files and folders in this path
# paths = [p for p in path.iterdir()]

# gets just directories in this path
# paths = [p for p in path.iterdir() if p.is_dir()]

# gets all .py files just in this path
# py_files = [p for p in path.glob("*.py")]

# gets all .py files recursively
# py_files = [p for p in path.rglob("*.py")]
```

## 6.3 Files

```python

```