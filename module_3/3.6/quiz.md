1. **What is the output of the following snippet?**
```python
 list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2
 
del list_1[0]
del list_2[0]
 
print(list_3) 
```

`["C"]`

2. **What is the output of the following snippet?**
```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2

print(list_3)
```

`["B", "C"]`

3. **What is the output of the following snippet?**
```python
list_1 = ["A", "B", "C"]
list_2 = list_1
list_3 = list_2

del list_1[0]
del list_2[:]

print(list_3)
```

`[]`

4. **What is the output of the following snippet?**
```python
list_1 = ["A", "B", "C"]
list_2 = list_1[:]
list_3 = list_2[:]

del list_1[0]
del list_2[0]

print(list_3)
```

`["A","B","C"]`

5. **Insert `in` or `not in` instead of `???` so that the code outputs the expected result.**
```python
my_list = [1, 2, "in", True, "ABC"]

print(1 in my_list)  # outputs True
print("A" not in my_list)  # outputs True
print(3 not in my_list)  # outputs True
print(False in my_list)  # outputs False
```