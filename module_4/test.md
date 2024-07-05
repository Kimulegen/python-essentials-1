1. **Which one of the following lines properly starts a parameterless function definition?**

    `def fun():`

2. **A function defined in the following way:  (Select two answers)**
    ```python
    def function(x=0):
        return x
    ```

    may be invoked without any argument

    may be invoked with exactly one argument

3. **A built-in function is a function which:**

    comes with Python, and is an integral part of Python

4. **The fact that tuples belong to sequence types means that:**

    they can be indexed and sliced like lists

5. **What is the output of the following snippet?**
    ```python
    def f(x):
        if x == 0:
            return 0
        return x + f(x - 1)


    print(f(3))
    ```

    `6`

6. **What is the output of the following snippet?**
    ```python
    def fun(x):
        x += 1
        return x


    x = 2
    x = fun(x + 1)
    print(x)
    ```  

    `4`

7. **What code would you insert instead of the comment to obtain the expected output?
Expected output:**
    ```
    a
    b
    c
    ```
    Code:
    ```python
    dictionary = {}
    my_list = ['a', 'b', 'c', 'd']

    for i in range(len(my_list) - 1):
        dictionary[my_list[i]] = (my_list[i], )

    for i in sorted(dictionary.keys()):
        k = dictionary[i]
        # Insert your code here.
    ```

    `print(k[0])`

8. **The following snippet:**
    ```python
    def func(a, b):
        return a ** a


    print(func(2))
    ```
    
    is erroneous

9. **The following snippet:**
    ```python
    def func_1(a):
        return a ** a


    def func_2(a):
        return func_1(a) * func_1(a)


    print(func_2(2))
    ```

    will output `16`


10. **Which of the following lines properly starts a function using two parameters, both with zeroed default values?**

    `def fun(a=0, b=0):`


11. **Which of the following statements are true? (Select two answers)**

    The `None` value can be compared with variables

    The `None` value can be assigned to variables

12. **What is the output of the following snippet?**
    ```python
    def fun(x):
        if x % 2 == 0:
            return 1
        else:
            return


    print(fun(fun(2)) + 1)
    ```

    the code will cause a runtime error

13. **What is the output of the following snippet?**
    ```python
    def fun(x):
        global y
        y = x * x
        return y


    fun(2)
    print(y)
    ```

    `4`

14. **What is the output of the following snippet?**
    ```python
    def any():
        print(var + 1, end='')


    var = 1
    any()
    print(var)
    ```

    `21`

15. **Assuming that `my_tuple` is a correctly created tuple, the fact that tuples are immutable means that the following instruction:**
    ```python
    my_tuple[1] = my_tuple[1] + my_tuple[0]
    ```

    is illegal

16. **What is the output of the following snippet?**
    ```python
    my_list =  ['Mary', 'had', 'a', 'little', 'lamb']


    def my_list(my_list):
        del my_list[3]
        my_list[3] = 'ram'


    print(my_list(my_list))
    ```

    no output, the snippet is erroneous

17. **What is the output of the following snippet?**
    ```python
    def fun(x, y, z):
        return x + 2 * y + 3 * z


    print(fun(0, z=1, y=3))
    ```

    `9`

18. **What is the output of the following snippet?**
    ```python
    def fun(inp=2, out=3):
        return inp * out


    print(fun(out=2))
    ```

    `4`

19. **What is the output of the following code?**
    ```python
    dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
    v = dictionary['one']

    for k in range(len(dictionary)):
        v = dictionary[v]

    print(v)
    ```

    `two`

20. **What is the output of the following code?**
    ```python
    tup = (1, 2, 4, 8)
    tup = tup[1:-1]
    tup = tup[0]
    print(tup)
    ```

    `2`

21. **Select the true statements about the try-except block in relation to the following example. (Select two answers.)**
    ```python
    try:
        # Some code is here...
    except:
        # Some code is here...
    ```

    If you suspect that a snippet may raise an exception, you should place it in the try block.

    The code that follows the `except` statement will be executed if the code in the `try` clause runs into an error.

22. **What is the output of the following code?**
    ```python
    try:
        value = input("Enter a value: ")
        print(value/value)
    except ValueError:
        print("Bad input...")
    except ZeroDivisionError:
        print("Very bad input...")
    except TypeError:
        print("Very very bad input...")
    except:
        print("Booo!")
    ```

    `Very very bad input...`