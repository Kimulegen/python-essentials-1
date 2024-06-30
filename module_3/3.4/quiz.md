1. **What is the output of the following snippet?**
    ```python
    lst = [1, 2, 3, 4, 5]
    lst.insert(1, 6)
    del lst[0]
    lst.append(1)

    print(lst)
    ```

    `[6,2,3,4,5,1]`

2. **What is the output of the following snippet?**
    ```python
    lst = [1, 2, 3, 4, 5]
    lst_2 = []
    add = 0

    for number in lst:
        add += number
        lst_2.append(add)

    print(lst_2)
    ```

    `[1, 3, 6, 10, 15]`

3. **What is the output of the following snippet?**
    ```python
    lst = []
    del lst
    print(lst)
    ```

    `NameError: name 'lst' is not defined`

4. **What is the output of the following snippet?**
    ```python
    lst = [1, [2, 3], 4]
    print(lst[1])
    print(len(lst))
    ```

    `[2, 3] 3`