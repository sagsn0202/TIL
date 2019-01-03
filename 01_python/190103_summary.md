# 190103

## Pythontutor에서 돌려보자!

```python
import copy

l1 = [1,2,3]
l2 = [4,5,l1]

c1 = l2
c2 = copy.copy(l2)
c3 = copy.deepcopy(l2)

l1[0] = 'a'
l2[0] = 'b'
```

