n = int(input("Digite um número inteiro positivo: "))

precisao = 0.00001
baixo = 0
alto = max(1, n)
meio = (baixo + alto) / 2

while abs(meio**2 - n) > precisao:
    if meio**2 < n:
        baixo = meio
    else:
        alto = meio
    meio = (baixo + alto) / 2

print(f"A raiz quadrada aproximada de {n} é {meio:.5f}")
