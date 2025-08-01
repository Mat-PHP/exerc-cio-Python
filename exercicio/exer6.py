idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Não eleitor")
elif 16 <= idade < 18 or idade >= 70:
    print("Voto facultativo")
else:
    print("Voto obrigatório")  