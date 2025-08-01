quantidade=int(input("quantos de prdutos"))
preco_unitario=float(input("digite  o valor de cada unidade "))

if quantidade >100:
    desconto=0.10
else:
    desconto=0.05
    valor_inicial= quantidade *preco_unitario
    valor_com_desconto= valor_inicial* (1-desconto)
    desconto_unitario=preco_unitario*desconto
    print("valor inicial:",valor_inicial)
    print("quantidade:",quantidade)
    print("valor final a pagar:",valor_com_desconto)
