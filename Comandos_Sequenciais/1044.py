lista=input().split(' ')

n1=int(lista[0])
n2=int(lista[1])

r1=n1%n2
r2=n2%n1

if r1==0 or r2==0:
    print("Sao Multiplos")

else:
    print("Nao sao Multiplos")
