nota=int(input("Informe sua nota: "))
if nota>=90:
    print("Excelente!")
elif nota<90 and nota>=75:
    print("Primeira Classe")
elif nota<75 and nota>=40:
    print("Média")
else:
    print("Reprovado")
