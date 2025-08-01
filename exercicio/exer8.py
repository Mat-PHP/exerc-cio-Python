numero = input("Digite um número inteiro positivo: ")
tem_par = False

for digito in numero:
    if int(digito) % 2 == 0:
        tem_par = True
        break

if tem_par:
    print("O número possui pelo menos um dígito par.")
else:
    print("O número não possui nenhum dígito par.")
