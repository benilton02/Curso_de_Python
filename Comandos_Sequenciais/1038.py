lista=input().split(' ')

codigo=int(lista[0])
qtd=int(lista[1])

if(codigo==1):
    qtd=qtd*4

if(codigo==2):
    qtd=qtd*4.5

if(codigo==3):
    qtd=qtd*5

if(codigo==4):
    qtd=qtd*2

if(codigo==5):
    qtd=qtd*1.5

print("Total: R$ %.2f" %qtd)
