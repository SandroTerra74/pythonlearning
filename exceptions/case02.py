name = "PythonX"
try:
    #statements that can raise the error
    print(name)
except NameError as e:
    # if there is NameError, then this block will be executed
    print("Some error occurred! Please contact the developer.", e)