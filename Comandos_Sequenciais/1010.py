lista = input().split(" ")

cod_a=int(lista[0])
qtd_a=int(lista[1])
valor_a=float(lista[2])

lista2 = input().split(" ")

cod_b=int(lista2[0])
qtd_b=int(lista2[1])
valor_b=float(lista2[2])

total= qtd_a*valor_a+qtd_b*valor_b

print("VALOR A PAGAR: R$ %.2f" %total)
