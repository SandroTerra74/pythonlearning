try:
    a = int(input("Enter a positive integer:_"))
    if a <= 0:
        raise ValueError("It is not a positive number!")
except ValueError as e:
    print(e)