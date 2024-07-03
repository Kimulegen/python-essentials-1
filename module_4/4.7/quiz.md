1. **What is the output of the following program if the user enters `0`?**
    ```python
    try:
        value = int(input("Enter a value: "))
        print(value/value)
    except ValueError:
        print("Bad input...")
    except ZeroDivisionError:
        print("Very bad input...")
    except:
        print("Booo!")
    ```

    `Very bad input...`

2. **What is the expected behavior of the following program if the user enters `0`?**
    ```python
    value = input("Enter a value: ")
    print(10/value)
    ```

    `TypeError`