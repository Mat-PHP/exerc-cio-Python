n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma -= i
    else:
        soma += i

print("Soma alternada de 1 até", n, "é:", soma)
