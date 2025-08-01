import random

numero_sorteado = random.randint(1, 10)

palpite1 = int(input("Adivinhe o número (entre 1 e 10): "))
if palpite1 == numero_sorteado:
    print("Parabéns! Você acertou de primeira!")
elif palpite1 < numero_sorteado:
    print("Dica: O número é maior.")
else:
    print("Dica: O número é menor.")

palpite2 = int(input("Tente novamente: "))
if palpite2 == numero_sorteado:
    print("Parabéns! Você acertou na segunda tentativa!")
else:
    print(f"Que pena! O número era {numero_sorteado}.")
