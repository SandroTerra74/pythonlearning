print("Operador de associação - member operator")
name='pythonx'
print("x está no nome? ",'x' in name)
print("s está no nome? ",'s' in name)
print("x não está no nome? ",'x' not in name)

print("Operador de identidade")
num1 = 5
num2 = 5
num3 = 6
print(id(num1))
print(id(num2))
print(id(num3))
print(num1 is num2)
print(num1 is num3)
print(num1 is num1)