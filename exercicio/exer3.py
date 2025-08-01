contador = 0
while True:
    numero = int(input("Digite um numero (0 Para encerrar) "))
    if numero == 0:
        break
    if numero > 0:
      contador += 1
      print("quantidade de numero positivo digitados:", contador)

