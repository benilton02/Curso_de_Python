sal=float(input())

if sal>=0 and sal<=400:
    nsal=sal*1.15
    r=nsal-sal
    print("Novo salario: %.2f" %nsal)
    print("Reajuste ganho: %.2f" %r)
    print("Em percentual: 15 %")

if sal>400 and sal<=800:
    nsal=sal*1.12
    r=nsal-sal
    print("Novo salario: %.2f" %nsal)
    print("Reajuste ganho: %.2f" %r)
    print("Em percentual: 12 %")

if sal>800 and sal<=1200:
    nsal=sal*1.1
    r=nsal-sal
    print("Novo salario: %.2f" %nsal)
    print("Reajuste ganho: %.2f" %r)
    print("Em percentual: 10 %")

if sal>1200 and sal<=2000:
    nsal=sal*1.07
    r=nsal-sal
    print("Novo salario: %.2f" %nsal)
    print("Reajuste ganho: %.2f" %r)
    print("Em percentual: 7 %")

if sal>2000:
    nsal=sal*1.04
    r=nsal-sal
    print("Novo salario: %.2f" %nsal)
    print("Reajuste ganho: %.2f" %r)
    print("Em percentual: 4 %")

