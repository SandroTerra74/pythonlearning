try:
    number1=int(input("Enter first number:_"))
    number2=int(input("Enter second number:_"))
    print("Division is: ", number1/number2)
except Exception as e:
    print("Ooops! You cannot divide a number by zero!!!")
finally:
    print("Thanks for using our Super Calculator!!!")