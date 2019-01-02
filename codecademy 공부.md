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

## O(n)

```python
memo = {1:1, 2:1}
def fibonacci(n):
    if n == 0:
        return 0
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]
```

## O(n)

```python
def fibonacci(n):
    a, b = 1, 0
    for i in range(n):
        a, b = b, a + b
    return b
```

## O(log(n))

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

