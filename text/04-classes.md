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


```python

```
