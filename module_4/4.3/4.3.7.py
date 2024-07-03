def is_prime(num):
    for i in range(2, int(num**0.5)):
        if not (num % i):
            return False

    return True


for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()
