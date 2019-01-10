# ~190110

## Class

### Attribute Function

*attributes*: Instance variables and class variables 

```python
class NoCustomAttributes:
  pass

attributeless = NoCustomAttributes()

try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
```

```python
hasattr(attributeless, "fake_attribute")
# returns False

getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value
```

```python
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

```

```python
class HoldsFive:
  five = 5
five_holder = HoldsFive()
hasattr(five_holder, 'five')
```

`hasattr()` returns a boolean that evaluates whether the given object has the attribute given by the second argument

The instance of the object itself. We usually refer to it as `self`.