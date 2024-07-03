1. **What is the output of the following snippet?**
```python
def intro(a="James Bond", b="Bond"):
     print("My name is", b + ".", a + ".")

intro()
```

`My name is Bond. James Bond.`

2. **What is the output of the following snippet?**
```python
def intro(a="James Bond", b="Bond"):
    print("My name is", b + ".", a + ".")

intro(b="Sean Connery")
```

`My name is Sean Connery. James Bond.`

3. **What is the output of the following snippet?**
```python
def intro(a, b="Bond"):
    print("My name is", b + ".", a + ".")

intro("Susan")
```

`My name is Bond. Susan.`

4. **What is the output of the following snippet?**
```python
def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)
```

`SyntaxError` - a non-default argument (`c`) follows a default argument (`b=2`).