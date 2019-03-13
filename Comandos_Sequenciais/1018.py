n=int(input())

cem=n//100

aux=n%100
cinquenta=aux//50
aux=aux%50

vinte=aux//20
aux=aux%20

dez=aux//10
aux=aux%10

cinco=aux//5
aux=aux%5

dois=aux//2
aux=aux%2

print(n)
print(cem,"nota(s) de R$ 100,00")
print(cinquenta,"nota(s) de R$ 50,00")
print(vinte,"nota(s) de R$ 20,00")
print(dez,"nota(s) de R$ 10,00")
print(cinco,"nota(s) de R$ 5,00")
print(dois,"nota(s) de R$ 2,00")
print(aux,"nota(s) de R$ 1,00")
