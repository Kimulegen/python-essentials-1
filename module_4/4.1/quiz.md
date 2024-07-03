1. **The `input()` function is an example of a:**

    a) user-defined function

    b) built-in function (✅)

2. **What happens when you try to invoke a function before you define it? Example:**
    ```python
    hi()

    def hi():
        print("hi!")
    ```

    An exception is thrown (the `NameError` exception to be more precise).

3. **What will happen when you run the code below?**
    ```python
    def hi():
        print("hi")

    hi(5)
    ```
    
    An exception will be thrown (the `TypeError` exception to be more precise) - the hi() function doesn't take any arguments.