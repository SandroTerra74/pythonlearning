print("Exemplo 01")
str = "Goodmorning"
for i in str:
    if i == "m":
        break
    else:
        print(i)
print("Exemplo 02")
n = int(input("Indique a capacidade máxima do navio:"))
threshold = n * (50.0 / 100.0)
for i in range(0,n,10):
    if i > threshold:
        print('50% da capacidade atingida!')
        break
    else:
        print('Passageiros embarcados: ', i)