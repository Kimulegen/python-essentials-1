1. **What is the output of the following snippet?**
```python
x = 1
y = 0

z = ((x == y) and (x == y)) or not(x == y)
print(not(z))
```
`False`

2. **What is the output of the following snippet?**
```python
x = 4
y = 1

a = x & y 
b = x | y 
c = ~x  # tricky! 1111111111111111011
d = x ^ 5 
e = x >> 2 
f = x << 2 

print(a, b, c, d, e, f)
```
`0 5 ? 1 1 16`