coeficientes=input().split(' ')

A=float(coeficientes[0])
B=float(coeficientes[1])
C=float(coeficientes[2])

delta = B**2-4*A*C

if (A!=0 and delta>0):
    R1= (-B + (delta)**.5)/(2*A)
    R2= (-B - (delta)**.5)/(2*A)

    print("R1 = %.5f" %R1)
    print("R2 = %.5f" %R2)

else:
    print("Impossivel calcular")
