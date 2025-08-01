l1 = int(input("Digite o valor do lado 1: "))
l2 = int(input("Digite o valor do lado 2: "))
l3 = int(input("Digite o valor do lado 3: "))
l4 = int(input("Digite o valor do lado 4: "))

if l1 == l2 == l3 == l4:
    print("É um quadrado")
elif l1 == l3 and l2 == l4:
    print("É um retângulo")
else:
    print("Não é quadrado nem retângulo")
