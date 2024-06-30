1. **An operator able to check whether two values are equal is coded as:**

    `==`

2. **The value eventually assigned to x is equal to:**
    ```python
    x = 1
    x = x == x
    ```

    `True`

3. **How many stars (`*`) will the following snippet send to the console?**
    ```python
    i = 0
    while i <= 3 :
        i += 2
        print("*")
    ```

    two

4. **How many stars (`*`) will the following snippet send to the console?**
    ```python
    i = 0
    while i <= 5 :
        i += 1
        if i % 2 == 0:
        break
        print("*")
    ```
    one

5. **How many hashes (`#`) will the following snippet send to the console?**
    ```python
    for i in range(1):
        print("#")
    else:
        print("#")
    ```

    two

6. **How many hashes (`#`) will the following snippet send to the console?**
    ```python
    var = 0
    while var < 6:
        var += 1
        if var % 2 == 0:
            continue
        print("#")
    ```

    three

7. **How many hashes (`#`) will the following snippet send to the console?**
    ```python
    var = 1
    while var < 10:
        print("#")
        var = var << 1
    ```

    four

8. **What value will be assigned to the `x` variable?**
    ```python
    z = 10
    y = 0
    x = y < z and z > y or y > z and z < y
    ```

    `True`

9. **What is the output of the following snippet?**
    ```python
    a = 1
    b = 0
    c = a & b
    d = a | b
    e = a ^ b

    print(c + d + e)
    ```

    `2`

10. **What is the output of the following snippet?**
    ```python
    my_list = [3, 1, -2]
    print(my_list[my_list[-1]])
    ```

    `1`

11. **What is the output of the following snippet?**
    ```python
    my_list = [1, 2, 3, 4]
    print(my_list[-3:-2])
    ```

    `[2]`

12. **The second assignment:**
    ```python
    vals = [0, 1, 2]
    vals[0], vals[2] = vals[2], vals[0]
    ```

    reverses the list

13. **After execution of the following snippet, the sum of all `vals` elements will be equal to:**
    ```python
    vals = [0, 1, 2]
    vals.insert(0, 1)
    del vals[1]
    ```

    `4`

14. **Take a look at the snippet, and choose the true statements: (Select two answers)**
    ```python
    nums = [1, 2, 3]
    vals = nums
    del vals[1:2]
    ```

    `nums` and `vals` refer to the same list

15. **Which of the following sentences are true? (Select two answers)**
    ```python
    nums = [1, 2, 3]
    vals = nums[-1:-2]
    ```

    `nums` and `vals` are two different lists

    `nums` is longer than `vals`

16. **What is the output of the following snippet?**
    ```python
    my_list_1 = [1, 2, 3]
    my_list_2 = []
    for v in my_list_1:
        my_list_2.insert(0, v)
    print(my_list_2)
    ```

    `[3, 2, 1]`

17. **What is the output of the following snippet?**
    ```python
    my_list = [1, 2, 3]
    for v in range(len(my_list)):
        my_list.insert(1, my_list[v])
    print(my_list)
    ```

    `[1, 1, 1, 1, 2, 3]`

18. **How many elements does the `my_list` list contain?**
    ```python
    my_list = [i for i in range(-1, 2)]
    ```

    three

19. **What is the output of the following snippet?**
    ```python
    t = [[3-i for i in range (3)] for j in range (3)]
    s = 0
    for i in range(3):
        s += t[i][i]
    print(s)
    ```

    `6`

20. **What is the output of the following snippet?**
    ```python
    my_list = [[0, 1, 2, 3] for i in range(2)]
    print(my_list[2][0])
    ```

    `the snippet will cause a runtime error`


