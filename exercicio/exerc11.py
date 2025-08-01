num1 = input("Digite o primeiro número inteiro positivo: ")
num2 = input("Digite o segundo número inteiro positivo: ")

menor_tamanho = min(len(num1), len(num2))
iguais = 0

for i in range(menor_tamanho):
    if num1[i] == num2[i]:
        iguais += 1

print("Quantidade de dígitos iguais na mesma posição:", iguais)
