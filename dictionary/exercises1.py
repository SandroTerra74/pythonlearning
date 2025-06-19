#Acessando elementos
example = {1:"John", 2:"Nick"}
print(example[1])
print(example.get(2))
#Atualizando elementos
example = {1:"John", 2:"Nick"}
example[1]="Den"
example[3]="Sam"
print(example)
#Deletando elementos
example = {1: 'Den', 2: 'Nick', 3: 'Sam'}
del example[3]
print(example)