# Perceptron Algorithm

https://medium.com/anubhav-shrimal/perceptron-algorithm-1b387058ecfb

For a point with coordinates (p,q)(*p*,*q*), label y*y*, and prediction given by the equation \hat{y} = step(w_1x_1 + w_2x_2 + b)*y*^=*step*(*w*1*x*1+*w*2*x*2+*b*):

- If the point is correctly classified, do nothing.
- If the point is classified positive, but it has a negative label, subtract \alpha p, \alpha q,*α**p*,*α**q*, and \alpha*α* from w_1, w_2,*w*1,*w*2,and b*b* respectively.
- If the point is classified negative, but it has a positive label, add \alpha p, \alpha q,*α**p*,*α**q*, and \alpha*α* to w_1, w_2,*w*1,*w*2, and b*b*respectively.

```
1. Start with random weights (W) and bias (b)
2. For every misclassified point (p1, p2, …, pn):
   2.1 if Red point (i.e. prediction = 1 WX+b ≥ 0 but should be < 0)
       For i <- 1 to n
          update wi <- wi - α * xi
          update b <- b - α
   2.2 if Blue point (i.e. prediction = 0 WX+b <0 but should be >=0)
       For i <- 1 to n
          update wi <- wi + α * xi
          update b <- b + α
3. end
```

```python
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    for i in range(len(X)):
        y_hat = prediction(X[i],W,b)
        if y[i]-y_hat == 1:
            W[0] += X[i][0]*learn_rate
            W[1] += X[i][1]*learn_rate
            b += learn_rate
        elif y[i]-y_hat == -1:
            W[0] -= X[i][0]*learn_rate
            W[1] -= X[i][1]*learn_rate
            b -= learn_rate
    return W, b
```

```python
X = [
    [x_1, y_1],
    [x_2, y_2],
    [x_3, y_3],
    [x_4, y_4]
]
```

```python
X.T = [
    [x_1, x_2, x_3, x_4],
    [y_1, y_2, y_3, y_4]
]
```

## Sigmoid Function

\sigma(WX + b)

## Softmax Function

```python
import numpy as np

def softmax(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i*1.0/sumExpL)
    return result
    
    # Note: The function np.divide can also be used here, as follows:
    # def softmax(L):
    #     expL = np.exp(L)
    #     return np.divide (expL, expL.sum())
```

## (Log-loss)Error Function

- The error function should be differentiable.
- The error function should be continuous.

## Maximizing Probabilities

Product(Bad) -> Sum(Good). Use logarithm!

## (Minimal)Cross-Entropy

```python
import numpy as np

# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy(Y, P):
    Y = np.asfarray(Y)
    P = np.asfarray(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
```

```python
import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))
```

A higher cross-entropy implies a lower probability for an event.

### Logistic Regression

- Take your data
- Pick a random model
- Calculate the error
- Minimize the error, and obtain a better model
- Enjoy!