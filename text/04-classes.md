# 4. Classes

- `Class`: a blueprint for creating new objects

- `Object`: an instance of a class

## 4.1 Definition

Naming Convention:

- PascalCase - First Character of each word is uppercase without space or underscore in between

```python
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))                  # <class '__main__.Point'>
print(isinstance(point, Point))     # True
```

## 4.2 Constructor

used to set attributes of an object or do something to initiate the object

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(3, 6)
point.draw()            # Point (3, 6)
```

## 4.3 Class Level Attributes

attributes defined in class level and can be accessed by all object as well as the class

```python
class Point:
    default_color = "red"

point = Point()
print(Point.default_color)  # red
print(point.default_color)  # red
```

## 4.4 Class Level Methods

methods defined in class level, demonstrated with a decorator, so using this method there is no need to make an object first. they can be accessed directly from the class

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()            # Point (0, 0)
```

## 4.5 Magic Methods

> ref: [Python 3 Magic Methods](https://rszalski.github.io/magicmethods/)


```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")

zero = Point.zero()
zero.draw()             # Point (0, 0)
print(zero)             # (0, 0)
point = Point(3, 48)
print(point)            # (3, 48)
```

## 4.6 Object Comparison

to compare 2 objects these methods below should be defined:

- `__eq__(self, other)`      -> ==
- `__ne__(self, other)`      -> !=
- `__gt__(self, other)`      -> >
- `__ge__(self, other)`      -> >=
- `__lt__(self, other)`      -> <
- `__le__(self, other)`      -> <=


```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

point1 = Point(3, 5)
point2 = Point(4, 8)

print(point1 == point2)     # False
print(point1 > point2)      # False
print(point1 < point2)      # True
print(point1 <= point2)     # True
print(point1 >= point2)     # False
print(point1 != point2)     # True
```

## 4.7 Arithmetic Magic Methods 

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

point1 = Point(3, 5)
point2 = Point(4, 8)

print(point1 + point2)     # (7, 13)
```

## 4.8 Making Custom Container

building tag container with these options:

- add a new tag (not case sensitive)

- retrieving value of a tag

- setting a value for a tag

- retrieving number of all tags

- make it iterable, so it could be iterated through loops

```python
class TagCloud:
    def __init__(self):
        self.tags = dict()

    def __len__(self):
        return len(self.tags)

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count if count > 0 else 0

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __iter__(self):
        return iter(self.tags)

    def __str__(self):
        return str(self.tags)

tags = TagCloud()
tags.add("python")
tags.add("Python")
tags.add("PythoN")

tags["javascript"] = 2
print(f"-> tags: {tags}")               # -> tags: {'python': 3, 'javascript': 2}
print(f"-> length: {len(tags)}")        # -> length: 2
for tag in tags:
    print(f"-> {tag}: {tags[tag]}")     # -> python: 3  -> javascript: 2
print(f"-> c++: {tags['c++']}")         # -> c++: 0
```

## 4.9 Private Members

```python
class TagCloud:
    def __init__(self):
        self.__tags = dict()            # __ -> makes conventionally this variable private, not really

    def __len__(self):
        return len(self.__tags)

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count if count > 0 else 0

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __iter__(self):
        return iter(self.__tags)

    def __str__(self):
        return str(self.__tags)


tags = TagCloud()
tags.add("python")
tags.add("Python")
tags.add("PythoN")

tags["javascript"] = 2
print(f"-> tags: {tags}")               # -> tags: {'python': 3, 'javascript': 2}
print(f"-> length: {len(tags)}")        # -> length: 2
for tag in tags:
    print(f"-> {tag}: {tags[tag]}")     # -> python: 3  -> javascript: 2
print(f"-> c++: {tags['c++']}")         # -> c++: 0

print(tags.__dict__)                    # a dictionary with all attributes of object inside
print(tags._TagCloud__tags)             # access to private member __tags
```

## 4.10 Properties

```python
class Product:
    def __init__(self, price=0):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price can not be negative")
        self.__price = value

prod = Product()
print(prod.price)       # 0
# prod.price = -10      # raise an error
prod.price = 25
print(prod.price)       # 25
```
