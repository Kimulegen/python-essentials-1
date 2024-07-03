1. **What is the output of the following snippet?**
    ```python
    def message():
        alt = 1
        print("Hello, World!")


    print(alt)
    ```

    ```
    NameError
    ```


2. **What is the output of the following snippet?**
    ```python
    a = 1


    def fun():
        a = 2
        print(a)


    fun()
    print(a)
    ```

    ```
    2
    1
    ```

3. **What is the output of the following snippet?**
    ```python
    a = 1


    def fun():
        global a
        a = 2
        print(a)


    fun()
    a = 3
    print(a)
    ```

    ```
    2
    3
    ```

4. **What is the output of the following snippet?**
    ```python
    a = 1


    def fun():
        global a
        a = 2
        print(a)


    a = 3
    fun()
    print(a)
    ```

    ```
    2
    2
    ```