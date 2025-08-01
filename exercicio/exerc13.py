nota = float(input("Digite a nota da prova (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota >= 9:
    print("Conceito: A")
elif nota >= 7:
    print("Conceito: B")
elif nota >= 5:
    print("Conceito: C")
elif nota >= 3:
    print("Conceito: D")
else:
    print("Conceito: E")
