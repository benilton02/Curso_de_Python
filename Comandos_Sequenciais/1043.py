lista=input().split(' ')

a=float(lista[0])
b=float(lista[1])
c=float(lista[2])

if a<b+c and b<a+c and c<a+b:
    perimetro=a+b+c
    print("Perimetro = %.1f" %perimetro)

else:
    area = (a+b)*c*.5
    print("Area = %.1f" %area)
