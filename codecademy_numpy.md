# NumPy: Python

- Efficiently working with many numbers at once
- Generating random numbers
- Performing many different numerical functions (i.e., calculating sin, cos, tan, mean, median, etc.)
- 명령어

```python
np.array(list)
np.genfromtxt("*.csv", delimiter=",")
a_plus_3 = a + 3
a_plus_b = a + b
a_square = a ** 2
np.sqrt(a)
```

## List vs Array

```python
# With a list
l = [1, 2, 3, 4, 5]
l_plus_3 = []
for i in range(len(l)):
    l_plus_3.append(l[i] + 3)
# l_plus_3 = [4, 5, 6, 7, 8]
```

```python
# With an array
a = np.array(l)
a_plus_3 = a + 3
# a_plus_3 = [4 5 6 7 8]
```

## Two-dimensional array

* Two-dimensional array is a list of lists where each list has the same number of elements.

```python
np.array([[92, 94, 88, 91, 87], 
          [79, 100, 86, 93, 91],
          [87, 85, 72, 90, 92]])
'''
[[ 92  94  88  91  87]
 [ 79 100  86  93  91]
 [ 87  85  72  90  92]]
'''
```

```python
np.array([[29, 49,  6], 
          [77,  1]])
'''
[list([29, 49, 6]) list([77, 1])]
'''
```

```python
np.array([68, 16, 73],
         [61, 79, 30])
'''
Traceback (most recent call last):
  File "script.py", line 19, in <module>
    [61, 79, 30])
TypeError: data type not understood
'''
```

```python
a = np.array([[32, 15, 6, 9, 14], 
              [12, 10, 5, 23, 1],
              [2, 16, 13, 40, 37]])

>>> a[2,1]
16

# selects the first column
>>> a[:,0]
array([32, 12,  2])

# selects the second row
>>> a[1,:]
array([12, 10,  5, 23,  1])

# selects the first three elements of the first row
>>> a[0,0:3]
array([32, 15,  6])
```

