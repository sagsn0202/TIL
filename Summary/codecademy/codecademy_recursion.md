# Recursion : Python

## Building our own Call Stack

```python
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
    
  print("BASE CASE REACHED")
  # tuple 값으로 return
  return result, call_stack

sum_to_one(4)
```

## Building our own Call Stack, Part II

```python
def sum_to_one(n):
  result = 1
  call_stack = []
  
  while n != 1:
    execution_context = {"n_value": n}
    call_stack.append(execution_context)
    n -= 1
    print(call_stack)
  print("BASE CASE REACHED")
  while len(call_stack) != 0:
    return_value = call_stack.pop()
    print(return_value["n_value"])
    print(call_stack)
  return result, call_stack

sum_to_one(4)
```

## Sum to One with Recursion

```python
# Define sum_to_one() below...
def sum_to_one(n):
  if n == 1:
    return n
  print("Recursing with input: {0}".format(n))
  return n + sum_to_one(n - 1)

# uncomment when you're ready to test
print(sum_to_one(7))
```

## Recursion and Big O

```python
# Define factorial() below:
def factorial(n):
  if n <= 1:
    return 1
  while n != 1:
    return n * factorial(n - 1)
  
print(factorial(12))
```

## Stack Over-Whoa!

### Power Set)

1. O(2^N)

```python
def power_set(set):
  power_set_size = 2**len(set)
  result = []

  for bit in range(0, power_set_size):
    sub_set = []
    for binary_digit in range(0, len(set)):
      if((bit & (1 << binary_digit)) > 0):
        sub_set.append(set[binary_digit])
    result.append(sub_set)
  return result
  
power_set(['a', 'b', 'c'])
```

2. Recursion

```python
def power_set(my_list):
  if len(my_list) == 0:
    return [[]]
  power_set_without_first = power_set(my_list[1:])
  with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
  return with_first + power_set_without_first
```

**No need to bring in a whole number system to find the solution!**

### Example)

```python
def power_set(my_list):
    # base case: an empty list
    if len(my_list) == 0:
        return [[]]
    # recursive step: subsets without first element
    power_set_without_first = power_set(my_list[1:])
    # subsets with first element
    with_first = [ [my_list[0]] + rest for rest in power_set_without_first ]
    # return combination of the two
    return with_first + power_set_without_first
  
universities = ['MIT', 'UCLA', 'Stanford', 'NYU']
power_set_of_universities = power_set(universities)

for set in power_set_of_universities:
  print(set)
```

## No Nested Lists Anymore, I Want Them to Turn Flat

```python
# define flatten() below...
def flatten(my_list):
  result = []
  for el in my_list:
    if isinstance(el, list):
      print("list found!")
      flat_list = flatten(el)
      result += flat_list
    else:
      result.append(el)
  return result


### reserve for testing...
planets = ['mercury', 'venus', ['earth'], 'mars', [['jupiter', 'saturn']], 'uranus', ['neptune', 'pluto']]
print(flatten(planets))
```

## Fibonacci

### O(c**n), c = golden ratio((1+root(5))/2)

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### O(n)

```python
memo = {1:1, 2:1}
def fibonacci(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
```

### O(n)

```python
def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b
```

### O(log(n))

```python
def mult(x,y):
    """
    행렬에 대한 곱셈 함수
    x, y = list 형태의 매트릭스
    """
    if ( len(y) == 2 ):
        a = x[0]*y[0] + x[1]*y[1]
        b = x[2]*y[0] + x[3]*y[1]
        return [a,b]
    a = x[0]*y[0] + x[1]*y[2]
    b = x[0]*y[1] + x[1]*y[3]
    c = x[2]*y[0] + x[3]*y[2]
    d = x[2]*y[1] + x[3]*y[3]
    return [a,b,c,d]

# 양수에만 적용됨
def matrix_power( x, n ):
    """
    행렬 지수 함수
    """
    # fibonacci(1) 이면 그대로 x를 반환
    if (n == 1):
        return x
    # n 이 짝수일 경우
    if (n % 2 == 0):
        return matrix_power(mult(x, x), n//2)
    # n 이 홀수일 경우
    return mult(x, matrix_power(mult(x, x), n//2))

# fibonacci example:
A = [1,1,1,0]
v = [1,0]

print(mult(matrix_power(A, n-1), v)[0])
```

## Recursive Data Structures

```python
# Define build_bst() below...
def build_bst(my_list):
  if my_list == []:
    return "No Child"
  else:
    middle_idx = len(my_list) // 2
    middle_value = my_list[middle_idx]
    print("Middle index: {}".format(middle_idx))
    print("Middle value: {}".format(middle_value))
    
    tree_node = {}
    tree_node["data"] = middle_value
    left_half_of_list = my_list[:middle_idx]
    right_half_of_list = my_list[middle_idx + 1:]
    tree_node["left_child"] = build_bst(left_half_of_list)
    tree_node["right_child"] = build_bst(right_half_of_list)
    
    return tree_node

# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
```

## Recursion vs Iteration

Anything we write iteratively, we can also write recursively, and vice versa. Often, the difference is substituting a loop for recursive calls.

### Factorial

#### Recursion

```python
def factorial(n):
  if n < 0:
    ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1

  return n * factorial(n - 1)
```

#### Iteration

```python
def factorial(n):
  result = 1
  if n < 0:    
    ValueError("Inputs 0 or greater only") 
  if n <= 1:    
    return 1 
  while n:
    result = result * n
    n -= 1
  return result
```

### Fibonacci

#### Recursion

```python
# runtime: Exponential - O(2^N)

def fibonacci(n):
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n

  return fibonacci(n - 1) + fibonacci(n - 2)
```

#### Iteration

```python
def fibonacci(n):
  fibs = [1, 1]
  if n <= len(fibs) - 1:
    return fibs[n]
  else:
    while n > len(fibs) - 1:
      next_fibs = fibs[-1] + fibs[-2]
      fibs.append(next_fibs)
    return fibs[n]
```

### Sum Digits

#### Recursion

```python
def sum_digits(n):
  if n <= 9:
    return n

  last_digit = n % 10
  return sum_digits(n // 10) + last_digit
```

#### Iteration

```python
# Linear - O(N)
def sum_digits(n):
  if n < 0:
    ValueError("Inputs 0 or greater only!")
  result = 0
  while n is not 0:
    result += n % 10
    n = n // 10
  return result + n
```

### Minimum

#### Recursion

```python
def find_min(my_list, min=None):
  if not my_list:
    return min

  if not min or my_list[0] < min:
    min = my_list[0]
  return find_min(my_list[1:], min)
```

#### Iteration

```python
def find_min(my_list):
  min = None
  for element in my_list:
    if not min or (element < min):
      min = element
  return min
```

### Palindromes

#### Recursion

```python
def is_palindrome(my_string):
  if len(my_string) <= 1:
    return True

  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])
```

#### Iteration

```python
def is_palindrome(my_string):
  while len(my_string) > 1:
    if my_string[0] != my_string[-1]:
      return False
    my_string = my_string[1:-1]
  return True 
```

```python
# Linear - O(N)
def is_palindrome(my_string):
  string_length = len(my_string)
  middle_index = string_length // 2
  for index in range(0, middle_index):
    opposite_character_index = string_length - index -1
    if my_string[index] != my_string[opposite_character_index]:
      return False  
  return True
```

### Multiplication

#### Recursion

```python
def multiplication(num_a, num_b):
  if num_a == 0 or num_b == 0:
    return 0

  return num_a + multiplication(num_a, num_b - 1)
```

#### Iteration

```python
def multiplication(num_1, num_2):
  result = 0
  for count in range(0, num_2):
    result += num_1
  return result
```

### Tower of Hanoi

#### Recursion

```python
# 아래에 코드를 작성해주세요.
def tower_of_hanoi(n, from_pil, to_pil, aux_pil):
    # base case
    if n == 1:
        print(from_pil, "->", to_pil)
        return
    #recursion case
    tower_of_hanoi(n - 1, from_pil, aux_pil, to_pil)
    print(from_pil, "->", to_pil)
    tower_of_hanoi(n - 1, aux_pil, to_pil, from_pil)
```

![tower_of_hanoi](C:\Users\student\TIL\Summary\codecademy\image\tower_of_hanoi.png)

### Binary Trees' Depth

#### Binary Trees

##### Example

```python
# first level
root_of_tree = {"data": 42}
# adding a child - second level
root_of_tree["left_child"] = {"data": 34}
root_of_tree["right_child"] = {"data": 56}
# adding a child to a child - third level
first_child = root_of_tree["left_child"]
first_child["left_child"] = {"data": 27}
```

##### Function(Recursion)

```python
def build_bst(my_list):
  if len(my_list) == 0:
    return None

  mid_idx = len(my_list) // 2
  mid_val = my_list[mid_idx]

  tree_node = {"data": mid_val}
  tree_node["left_child"] = build_bst(my_list[ : mid_idx])
  tree_node["right_child"] = build_bst(my_list[mid_idx + 1 : ])

  return tree_node
```

#### Recursion

```python
def depth(tree_node):
  if tree_node == None:
    return 0
  
  left_depth = depth(tree_node["left_child"])
  right_depth = depth(tree_node["right_child"])
  
  if left_depth > right_depth:
    return left_depth + 1
  else:
    return right_depth + 1
```

#### Iteration

```python
def depth(tree):
  result = 0
  # our "queue" will store nodes at each level
  queue = [tree]
  # loop as long as there are nodes to explore
  while queue:
    # count the number of child nodes
    level_count = len(queue)
    for child_count in range(0, level_count):
      # loop through each child
      child = queue.pop(0)
     # add its children if they exist
      if child.get("left_child"):
        queue.append(child["left_child"])
      if child.get("right_child"):
        queue.append(child["right_child"])
    # count the level
    result += 1
  return result
```

