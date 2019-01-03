# Sorting Algorithm in Python

## Bubble Sort

### My Answer 

```python
nums = [5, 2, 9, 1, 5, 6]

def swap(arr, index_1, index_2):
    temp = arr[index_1]
    arr[index_1] = arr[index_2]
    arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
    # 완벽하지는 않다. for elem 경우 5 -> 6 -> 9로 진행한다.
    # This implementation will iterate through elements which have already been correctly placed.
    for elem in arr:
        for index in range(len(arr) - 1):
            if arr[index] > arr[index + 1]:
                swap(arr, index, index + 1)

##### test statements
print("Pre-Sort: {0}".format(nums))      
bubble_sort(nums)
print("Post-Sort: {0}".format(nums))
```

### Instructor Answer

```python
nums = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print("PRE SORT: {0}".format(nums))

def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp

def bubble_sort_unoptimized(arr):
  iteration_count = 0
  for el in arr:
    for index in range(len(arr) - 1):
      iteration_count += 1
      if arr[index] > arr[index + 1]:
        swap(arr, index, index + 1)

  print("PRE-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

def bubble_sort(arr):
  iteration_count = 0
  for i in range(len(arr)):
    # iterate through unplaced elements
    for idx in range(len(arr) - i - 1):
      iteration_count += 1
      if arr[idx] > arr[idx + 1]:
        # replacement for swap function
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]
        
  print("POST-OPTIMIZED ITERATION COUNT: {0}".format(iteration_count))

bubble_sort_unoptimized(nums.copy())
bubble_sort(nums)
print("POST SORT: {0}".format(nums))
```

## Merge Sort

```python
def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]

  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

def merge(left, right):
  result = []

  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)

  if left:
    result += left
  if right:
    result += right

  return result

unordered_list1 = [356, 746, 264, 569, 949, 895, 125, 455]
unordered_list2 = [787, 677, 391, 318, 543, 717, 180, 113, 795, 19, 202, 534, 201, 370, 276, 975, 403, 624, 770, 595, 571, 268, 373]
unordered_list3 = [860, 380, 151, 585, 743, 542, 147, 820, 439, 865, 924, 387]

ordered_list1 = merge_sort(unordered_list1)
ordered_list2 = merge_sort(unordered_list2)
ordered_list3 = merge_sort(unordered_list3)

print(ordered_list1)
print(ordered_list2)
print(ordered_list3)
```

**1. Remember a list is truthy if it has elements and falsy if it's empty**

**2. In `merge_sort()` create two new variables: `left_sorted` and `right_sorted`.**

**`left_sorted` should be the result of calling `merge_sort()`recursively on `left_split`.**

**`right_sorted` should be the result of calling `merge_sort()`recursively on `right_split`.**

**3. Return the result of calling `merge()` on `left_sorted` and `right_sorted`.**

## Quick Sort

**A sorted data-set : O(n^2)**

* the benefit of randomly selecting a pivot element in quicksort : A random pivot element removes the possibility that any one data-set will result in a poor Big O runtime.
* If the first element is always chosen as the pivot and the data-set is sorted, this would result in a `O(n^2)` runtime because the partition step only reduces the problem by a single element.

**An unsorted data-set : O(n*logn)**

