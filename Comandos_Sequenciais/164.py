i=0
while True:
    i=i+1

    dados=input().split(' ')
    r = int(dados[0])

    if r==0:
        break
        
    w = int(dados[1])
    l = int(dados[2])

    d = (w**2+l**2)**(.5)
    
    if d == 2*r:
        print("Pizza",i,"fits on the table.")
    
    if d < 2*r:
        print("Pizza",i,"fits on the table.")

    if d > 2*r:
        print("Pizza",i,"does not fit on the table.")

    
    


