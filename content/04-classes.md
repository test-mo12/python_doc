# 4. Classes

- `Class`: a blueprint for creating new objects

- `Object`: an instance of a class

## 4.1 Definition

- naming convention: PascalCase - First Character of each word is uppercase without space or underscore in between

```python
class Point:
    def draw(self):
        print("draw")

point = Point()
print(type(point))                  # <class '__main__.Point'>
print(isinstance(point, Point))     # True
```