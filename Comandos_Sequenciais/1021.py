n=float(input())

cedula=int(n)
moeda=int(100*(n-cedula))

#Quantidade mínima de cédulas:
aux=0
cem=cedula//100
aux=cedula%100

cinquenta=aux//50
aux=aux%50

vinte=aux//20
aux=aux%20

dez=aux//10
aux=aux%10

cinco=aux//5
aux=aux%5

dois=aux//2

print("NOTAS:")
print(cem, "nota(s) de R$ 100.00")
print(cinquenta,"nota(s) de R$ 50.00")
print(vinte,"nota(s) de R$ 20.00")
print(dez,"nota(s) de R$ 10.00")
print(cinco,"nota(s) de R$ 5.00")
print(dois,"nota(s) de R$ 2.00")


#Quantidade mínima de moedas:
_1real=aux%2

_50centavos=moeda//50
aux=moeda%50

_25centavos=aux//25
aux=aux%25

_10centavos=aux//10
aux=aux%10

_5centavos=aux//5
aux=aux%5


print("MOEDAS:")
print(_1real, "moeda(s) de R$ 1.00")
print(_50centavos, "moeda(s) de R$ 0.50")
print(_25centavos, "moeda(s) de R$ 0.25")
print(_10centavos, "moeda(s) de R$ 0.10")
print(_5centavos, "moeda(s) de R$ 0.05")
print(aux,"moeda(s) de R$ 0.01")

