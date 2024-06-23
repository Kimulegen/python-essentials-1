1. **What is the output of the following program?**

    ```python
    print("My\nname\nis\nBond.", end=" ")
    print("James Bond.")
    ```
    ```
    My
    name
    is
    Bond. James Bond.
    ```

2. **What is the output of the following program?**
    ```python
    print(sep="&", "fish", "chips")
    ```
    ```
      File "main.py", line 1
        print(sep="&", "fish", "chips")
                    ^
    SyntaxError: positional argument follows keyword argument
    ```

3. **Which of the following print() function invocations will cause a SyntaxError?**
    ```
    print('Greg\'s book.')
    print("'Greg's book.'")
    print('"Greg\'s book."')
    print("Greg\'s book.")
    print('"Greg's book."')
    ```

    Line 5 will raise `SyntaxError`, because the `'` symbol in the `Greg's book`. string requires an escape character.

