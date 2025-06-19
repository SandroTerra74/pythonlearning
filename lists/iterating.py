# Listando frutas
fruits = ["Apple", "Mango", "Cherry", "Banana"]
for i in fruits:
    print(i)
# Verificando se uma fruta está na lista
fruits = ["Apple", "Mango", "Cherry", "Banana"]
for i in fruits:
    if i == "Mango":
        print("Mango found")
        break
    else:
        print("Mango not found")