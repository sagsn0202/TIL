## Palindrome

```python
def palindrome_1(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return palindrome_1(string[1:-1])
```

```python
def palindrome_2(string):
    lower = string.lower()
    for i in range(len(str // 2)):
        if lower[i] != lower[-i - 1]:
            return False
    return True
```

```python
def palindrome_3(string):
    punctuation = [',', '!', '?', '.']
    no_punc_str = string[:]
    for punc in punctuation:
        no_punc_str = no_punc_str.replace(punc, '')
    for i in range(len(no_punc_str) // 2):
        if no_punc_str[i] != no_punc_str[-i - 1]:
            return False
    return True
```

```python
def palindrome_4(string):
    no_space_str = string.replace(' ', '')
    for i in range(len(no_space_str) // 2):
        if no_space_str[i] != no_space_str[-i - 1]:
            return False
    return True
```

## List Rotate

### Slice

```python
def rotate(my_list, num_rotations):
  return my_list[-num_rotations:] + my_list[:-num_rotations]
```

### Indices

Single variable declarations are considered `O(1)` *space*.

```python
def rev(lst, low, high):
    while low < high:
        lst[low], lst[high] = lst[high], lst[low]
        high -= 1
        low += 1
    return lst
```

```python
def rotate(my_list, num_rotations):
  # first half
  rev(my_list, 0, num_rotations - 1)

  # second half
  rev(my_list, num_rotations, len(my_list) - 1)

  # whole list
  rev(my_list, 0, len(my_list) - 1)
  return my_list
```

## Rotation Point

### My Answer

```python
def rotation_point(rotated_list):
  sorted_list = sorted(rotated_list)
  for idx in range(len(rotated_list)):
    if sorted_list == rotated_list[idx:] + rotated_list[:idx]:
      return idx
```

### Linear Search

```python
def rotation_point(rotated_list):
  rotation_idx = 0
  for i in range(len(rotated_list)):
    if rotated_list[i] < rotated_list[rotation_idx]:
      rotation_idx = i
  return rotation_idx
```

### Binary Search

*Binary search* is an algorithm which finds a target value in sorted datasets in `O(logN)` time.

```python
def rotation_point(rotated_list):
  low = 0
  high = len(rotated_list) - 1
  while low <= high:
    mid = (low + high) // 2
    mid_next = (mid + 1) % len(rotated_list)
    mid_previous = (mid - 1) % len(rotated_list)
    
    if (rotated_list[mid] < rotated_list[mid_previous]) and (rotated_list[mid] < rotated_list[mid_next]):
      return mid
    elif rotated_list[mid] < rotated_list[high]:
      high = mid - 1
    else:
      low = mid + 1
```

## Remove Duplicates

### Naive

`O(N)` time and/or `O(N)` space complexity.

```python
def remove_duplicates(dupe_list):
  result = []
  for el in dupe_list:
    if not el in result:
      result.append(el)
  return result
```

### Optimized

can't improve the time complexity, reduce the space complexity to `O(1)`

```python
def move_duplicates(dupe_list):
  unique_idx = 0
  for i in range(len(dupe_list) - 1):
    if dupe_list[i] != dupe_list[i + 1]:
      dupe_list[i], dupe_list[unique_idx] = dupe_list[unique_idx], dupe_list[i]
      unique_idx += 1
  dupe_list[unique_idx], dupe_list[len(dupe_list) - 1] = dupe_list[len(dupe_list) - 1], dupe_list[unique_idx]
  return unique_idx
```

## Max list sub-sum

### Naive

```python
def maximum_sub_sum(my_list):
  max_sum = my_list[0]
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      sub_sum = sum(my_list[i:j + 1])
      if sub_sum > max_sum:
        max_sum = sub_sum
  return max_sum
```

### Optimized

```python
def maximum_sub_sum(my_list):
  if max(my_list) < 0:
    return max(my_list)
  
  max_sum = 0
  max_sum_tracker = 0
  for i in range(len(my_list)):
    max_sum_tracker += my_list[i]
    if my_list[i] < 0:
      max_sum_tracker = 0
    if max_sum_tracker > max_sum:
      max_sum = max_sum_tracker
    
  return max_sum
```

## Pair Sum

### Naive

```python
def pair_sum(my_list, target):
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      if my_list[i] + my_list[j] == target:
        return [i, j]
  return None
```

### My Answer

```python
def pair_sum(my_list, target):
  for i in range(len(my_list)):
    search = target - my_list[i]
    if search in my_list:
      return [i, my_list.index(search)]
```