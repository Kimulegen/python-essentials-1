1. **What will happen when you attempt to run the following snippet and why?**
    ```python
    def factorial(n):
        return n * factorial(n - 1)


    print(factorial(4))
    ```

    `RecursionError: maximum recursion depth exceeded`

2. **What is the output of the following snippet?**
    ```python
    def fun(a):
        if a > 30:
            return 3
        else:
            return a + fun(a + 3)


    print(fun(25))
    ```

    ```
    56
    ```