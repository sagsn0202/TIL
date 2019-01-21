# NumPy: Python

- https://docs.scipy.org/doc/numpy/reference/
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

* `axis=0` are the values that share an index, `axis=1` are the values that share an array.(axis=0 as the columns and axis=1 as the rows)
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

## Logical Operation

```python
>>> a = np.array([10, 2, 2, 4, 5, 3, 9, 8, 9, 7])
>>> a > 5
array([True, False, False, False, False, False, True, True, True, True], dtype=bool)
```

```python
>>> a[a > 5]
array([10, 9, 8, 9, 7])
```

```python
>>> a[(a > 5) | (a < 2)]
array([10, 9, 8, 9, 7])
```

``` python
recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)
eggs = recipes[:, 2]
print(eggs)
one_egg = recipes[(eggs == 1)]
print(one_egg)
[[ 2.     0.75   2.     1.     0.5  ]
 [ 1.     0.125  1.     1.     0.125]
 [ 2.75   1.5    1.     0.     1.   ]
 [ 4.     0.5    2.     2.     0.5  ]]
[ 2.  1.  1.  2.]
[[ 1.     0.125  1.     1.     0.125]
 [ 2.75   1.5    1.     0.     1.   ]]
```



## Summary

- Arrays are a special type of list that allows us to store values in an organized manner.
- An array can be created by either defining it directly using `np.array()` or by importing a CSV using `np.genfromtxt('file.csv', delimiter=',')`.
- An operation (such as addition) can be performed on every element in an array by simply performing it on the array itself.
- Elements can be selected from arrays using their index and array locations, both of which start at 0.
- Logical operations can be used to create new, more focused arrays out of larger arrays.

## Basic Analysis

### Mean: 평균

```python
>>> survey_array = np.array(survey_responses)
>>> np.mean(survey_array)
```

```python
>>> np.mean(survey_array > 8)
0.2 # calculate the percent of array elements that have a certain property
```

```python
>>> ring_toss = np.array([[1, 0, 0], 
                          [0, 0, 1], 
                          [1, 0, 1]])
# mean across all the arrays
>>> np.mean(ring_toss)
0.44444444444444442
# means of each interior array, specify axis 1 (the "rows")
>>> np.mean(ring_toss, axis=1)
array([ 0.33333333,  0.33333333,  0.66666667])
# means of each index position, specify axis 0 (the "columns")
>>> np.mean(ring_toss, axis=0)
array([ 0.66666667,  0.        ,  0.66666667])
```

### Outliers: 이상치

```python
>>> heights = np.array([49.7, 46.9, 62, 47.2, 47, 48.3, 48.7])
>>> np.sort(heights)
array([ 46.9,  47. ,  47.2,  48.3,  48.7,  49.7,  62])
```

### Median: 중앙값

```python
>>> my_array = np.array([50, 38, 291, 59, 14])
>>> np.median(my_array)
50.0
```

### Percentiles: 백분위수

```python
>>> d = np.array([1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8])
>>> np.percentile(d, 40)
4.00
```

- The **25th percentile** is called the *first quartile*
- The **50th percentile** is called the *median*
- The **75th percentile** is called the *third quartile*

* The minimum, first quartile, median, third quartile, and maximum of a dataset are called a *five-number summary*.

* The difference between the first and third quartile is a value called the *interquartile range*. 

### Standard Deviation: 표준편차

```python
>>> nums = np.array([65, 36, 52, 91, 63, 79])
>>> np.std(nums)
17.716909687891082
```

## Summary

- Using the `np.sort` method to locate outliers.
- Calculating central positions of a dataset using `np.mean` and `np.median`.
- Understanding the spread of our data using **percentiles** and the **interquartile range**. 
- Finding the standard deviation of a dataset using `np.std`.

## Histograms

```python
commutes = np.genfromtxt('commutes.csv', delimiter=',')
plt.hist(commutes, range=(20, 51), bins=6)
plt.show()
```

`range`:  the minimum and maximum values

`bins`: different number of bins

## Distribution

![unimodal_new](C:\Users\student\TIL\Summary\codecademy\image\unimodal_new.png)

![bimodal_new](C:\Users\student\TIL\Summary\codecademy\image\bimodal_new.png)

![multimodal_new](C:\Users\student\TIL\Summary\codecademy\image\multimodal_new.png)

![uniform_new](C:\Users\student\TIL\Summary\codecademy\image\uniform_new.png)

![distribution-types-ii-symmetric](C:\Users\student\TIL\Summary\codecademy\image\distribution-types-ii-symmetric.png)

![distribution-types-ii-skew-right](C:\Users\student\TIL\Summary\codecademy\image\distribution-types-ii-skew-right.png)

![distribution-types-ii-skew-left](C:\Users\student\TIL\Summary\codecademy\image\distribution-types-ii-skew-left.png)

## Normal Distribution

![normal_distribution](C:\Users\student\TIL\Summary\codecademy\image\normal_distribution.png)

```python
a = np.random.normal(0, 1, size=100000)
```

 `np.random.normal`:  generate a set of numbers that fit a normal distribution

- **loc:** the mean for the normal distribution
- **scale:** the standard deviation of the distribution
- **size:** the number of random numbers to generate

Standard Deviations

- **68%** of our samples will fall between +/- 1 standard deviation of the mean
- **95%** of our samples will fall between +/- 2 standard deviations of the mean
- **99.7%** of our samples will fall between +/- 3 standard deviations of the mean

## Binomial Distribution

```python
# Let's generate 10,000 "experiments"
# N = 10 shots
# P = 0.30 (30% he'll get a free throw)

a = np.random.binomial(10, 0.30, size=10000)
plt.hist(a, range=(0, 10), bins=10, normed=True)
plt.xlabel('Number of "Free Throws"')
plt.ylabel('Frequency')
plt.show()
```

- **N**: The number of samples or trials
- **P**: The probability of success 
- **size**: The number of experiments

```python
a = np.random.binomial(10, 0.30, size=10000)
np.mean(a == 4)
>> 0.1973
```

*Remember that taking the mean of a logical statement will give us the percent of values that satisfy our logical statement.* 

*Remember, because we're using a random number generator, we'll get a slightly different result each time.  With the large* `size` *we chose, the calculated probability should be accurate to about 2 decimal places.*

**So, our basketball player has a roughly 20% chance of making 4 baskets.**

#### Python2

If you do not include below, Python will assume you want integer division (an integer divided by an integer). Naturally, integer division returns an integer.

* float()
* period