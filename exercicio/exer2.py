peso= float(input("digite seu peso: "))
altura = float(input("digite sua altura(m): "))
imc=peso/(altura**2)
print(f"seu imc e: {imc:.2f}")
if imc < 18.5:
    print("classifica: baixo do peso")
elif 18.5 <= imc <= 24.9:
    print("classifica: peso normal")
elif 25 <= imc <= 29.9:
    print("classifica: sobrepeso")
elif 30 <= imc <= 34.9:
    print("classifica: obesidade")
elif 35 <= imc <= 39.9:
    print("classifica: obesidade morbida")
elif 40 > imc <= 49.9:
    print("classifica: obesidade maior")
else:
    print("classifica: obesidade morbida")