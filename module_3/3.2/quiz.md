1. **Create a `for` loop that counts from 0 to 10, and prints odd numbers to the screen.**
    ```python
    for i in range(1,11):
        if i % 2 == 1:
            print(i)
    ```

2. **Create a `while` loop that counts from 0 to 10, and prints odd numbers to the screen.**
    ```python
    x = 1
    while x < 11:
        if x % 2 == 1:
            print(i)
        x += 1
    ```

3. **Create a program with a `for` loop and a `break` statement. The program should iterate over characters in an email address, exit the loop when it reaches the `@` symbol, and print the part before `@` on one line.**
    ```python
    email = ""
    for ch in "john.smith@pythoninstitute.org":
        if ch == "@":
            break
        email += ch
    print(email)
    ```

4. **Create a program with a `for` loop and a `continue` statement. The program should iterate over a string of digits, replace each `0` with `x`, and print the modified string to the screen.**
    ```python
    string = ''
    for digit in "0165031806510":
        if digit == "0":
            string += 'x'
            continue
        string += 'digit' 

    print(string)
    ```

5. **What is the output of the following code?**
    ```python
    n = 3
    
    while n > 0:
        print(n + 1)
        n -= 1
    else:
        print(n) 
    ```
    `4 3 2 0`

6. **What is the output of the following code?**
    ```python
    n = range(4)
    
    for num in n:
        print(num - 1)
    else:
        print(num) 
    ```
    `-1 0 1 2 3`

7. **What is the output of the following code?**
    ```python
    for i in range(0, 6, 3):
        print(i)
    ```
    `0 3`