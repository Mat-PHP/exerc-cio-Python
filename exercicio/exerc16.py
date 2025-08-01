texto = input("Digite uma frase: ")
caractere = input("Digite um caractere para contar: ")

contador = 0
for c in texto:
    if c == caractere:
        contador += 1

print(f"O caractere '{caractere}' aparece {contador} vezes.")
