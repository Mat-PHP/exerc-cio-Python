hora = int(input("Digite a hora (0 a 23): "))
minutos = int(input("Digite os minutos (0 a 59): "))
segundos = int(input("Digite os segundos (0 a 59): "))

if 0 <= hora < 24 and 0 <= minutos < 60 and 0 <= segundos < 60:
    print("Hora válida")
else:
    print("Hora inválida")
