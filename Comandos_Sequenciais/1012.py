while 1:
    dados=input().split(' ')
    a=float(dados[0])
    b=float(dados[1])
    c=float(dados[2])

    triangulo=a*c*.5
    circulo=3.14159*c**2
    trapezio=(a+b)*c*.5
    quadrado=b*b
    retangulo=a*b

    print("TRIANGULO: %.3f" %triangulo)
    print("CIRCULO: %.3f" %circulo)
    print("TRAPEZIO: %.3f" %trapezio)
    print("QUADRADO: %.3f" %quadrado)
    print("RETANGULO: %.3f" %retangulo)
    

    

