1. **What is the output of the following snippet?**
    ```python
    my_list = [1, 2]

    for v in range(2):
        my_list.insert(-1, my_list[v])

    print(my_list)
    ```

    `[1, 1, 1, 2]`

2. **The meaning of a _positional argument_ is determined by:**

    its position within the argument list

3. **Which of the following sentences are true about the code? (Select two answers)**

    nums has the same length as vals

    nums and vals are different names of the same list

4. **An operator able to check whether two values are not equal is coded as:**

    `!=`

5. **The following snippet:**
    ```python
    def function_1(a):
        return None


    def function_2(a):
        return function_1(a) * function_1(a)


    print(function_2(2))
    ```

    will cause a runtime error 

6. **The result of the following division:**
    ```python
    1 // 2
    ```

    is equal to `0`

7. **The following snippet:**
    ```python
    def func(a, b):
        return b ** a


    print(func(b=2, 2))
    ```

    is erroneous

8. **What value will be assigned to the `x` variable?**
    ```python
    z = 0
    y = 10
    x = y < z and z > y or y < z and z < y
    ```

    `False`

9. **Which of the following variable names are illegal and will cause the SyntaxError exception? (Select two answers)**

    `in`

    `for`

10. **What is the output of the following snippet?**
    ```python
    my_list =  [x * x for x in range(5)]


    def fun(lst):
        del lst[lst[2]]
        return lst


    print(fun(my_list))
    ```

    `[0, 1, 4, 9]`

11. **What is the output of the following piece of code?**
    ```python
    x = 1
    y = 2
    x, y, z = x, x, y
    z, y, z = x, y, z

    print(x, y, z)
    ```

    `1 1 2`

12. **What will be the output of the following snippet?**
    ```python
    a = 1
    b = 0
    a = a ^ b
    b = a ^ b
    a = a ^ b

    print(a, b)
    ```

    `0 1`

13. **What is the output of the following snippet?**
    ```python
    def fun(x):
        if x % 2 == 0:
            return 1
        else:
            return 2


    print(fun(fun(2)))
    ```

    `2`

14. **Take a look at the snippet and choose the true statement:**
    ```python
    nums = [1, 2, 3]
    vals = nums
    del vals[:]
    ```

    `nums` and `vals` have the same length

15. **What is the output of the following piece of code if the user enters two lines containing `3` and `2` respectively?**
    ```python
    x = int(input())
    y = int(input())
    x = x % y
    x = x % y
    y = y % x
    print(y)
    ```

    `0`

16. **What is the output of the following piece of code if the user enters two lines containing `3` and `6` respectively?**
    ```python
    y = input()
    x = input()
    print(x + y)
    ```

    `63`

17. **What is the output of the following piece of code?**
    ```python
    print("a", "b", "c", sep="sep")
    ```

    `asepbsepc`

18. **What is the output of the following piece of code?**
    ```python
    x = 1 // 5 + 1 / 5
    print(x)
    ```

    `0.2`

19. **Assuming that `my_tuple` is a correctly created tuple, the fact that tuples are immutable means that the following instruction:**
    ```python
    my_tuple[1] = my_tuple[1] + my_tuple[0]
    ```

    is illegal

20. **What is the output of the following piece of code if the user enters two lines containing `2` and `4` respectively?**
    ```python
    x = float(input())
    y = float(input())
    print(y ** (1 / x))
    ```

    `2.0`

21. **What is the output of the following snippet?**
    ```python
    dct = {'one': 'two', 'three': 'one', 'two': 'three'}
    v = dct['three']

    for k in range(len(dct)):
        v = dct[v]

    print(v)
    ```

    `one`

22. **How many elements does the `lst` list contain?**
    ```python
    lst = [i for i in range(-1, -2)]
    ```

    `zero`

23. **Which of the following lines correctly invoke the function defined below? (Select two answers)**
    ```python
    def fun(a, b, c=0):
        # Body of the function.
    ```

    `fun(b=0, a=0)`

    `fun(0, 1, 2)`

24. **What is the output of the following snippet?**
    ```python
    def fun(x, y):
        if x == y:
            return x
        else:
            return fun(x, y-1)


    print(fun(0, 3))
    ```

    `0`

25. **How many stars (`*`) will the following snippet send to the console?**
    ```python
    i = 0
    while i < i + 2 :
        i += 1
        print("*")
    else:
        print("*")
    ```

    the snippet will enter an infinite loop, printing one star per line

26. **What is the output of the following snippet?**
    ```python
    tup = (1, 2, 4, 8)
    tup = tup[-2:-1]
    tup = tup[-1]
    print(tup)
    ```

    `4`

27. **What is the output of the following snippet?**
    ```python
    dd = {"1": "0", "0": "1"}
    for x in dd.vals():
        print(x, end="")
    ```

    the code is erroneous (the `dict` object has no `vals()` method)

28. **What is the output of the following snippet?**
    ```python
    dct = {}
    dct['1'] = (1, 2)
    dct['2'] = (2, 1)

    for x in dct.keys():
        print(dct[x][1], end="")
    ```

    `21`

29. **What is the output of the following snippet?**
    ```python
    def fun(inp=2, out=3):
        return inp * out


    print(fun(out=2))
    ```

    `4`

30. **How many hashes (`#`) will the following snippet send to the console?**

    three

31. **What is the output of the following code if the user enters a `0`?**
    ```python
    try:
        value = input("Enter a value: ")
        print(int(value)/len(value))
    except ValueError:
        print("Bad input...")
    except ZeroDivisionError:
        print("Very bad input...")
    except TypeError:
        print("Very very bad input...")
    except:
        print("Booo!")
    ```

    `0.0`

32. **What is the expected behavior of the following program?**
    ```python
    try:
        print(5/0)
        break
    except:
        print("Sorry, something went wrong...")
    except (ValueError, ZeroDivisionError):
        print("Too bad...")
    ```

    The program will cause a `SyntaxError` exception.

33. **What is the expected behavior of the following program?**
    ```python
    foo = (1, 2, 3)
    foo.index(0)
    ```

    The program will cause a `ValueError` exception.

34. **Which of the following snippets shows the correct way of handling multiple exceptions in a single except clause?**
    ```python
    # A:
    except (TypeError, ValueError, ZeroDivisionError):
    # Some code.

    # B:
    except TypeError, ValueError, ZeroDivisionError:
    # Some code.

    # C:
    except: (TypeError, ValueError, ZeroDivisionError)
    # Some code.

    # D:
    except: TypeError, ValueError, ZeroDivisionError
    # Some code.

    # E:
    except (TypeError, ValueError, ZeroDivisionError)
    # Some code.

    # F:
    except TypeError, ValueError, ZeroDivisionError
    # Some code.
    ```

    A only

35. **What will happen when you attempt to run the following code?**
    ```python
    print(Hello, World!)
    ```

    The code will raise the _SyntaxError_ exception.
