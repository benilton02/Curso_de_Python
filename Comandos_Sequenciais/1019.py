tempo=int(input())

horas=tempo//3600
horas=str(horas)
aux=tempo%3600

minutos=aux//60
minutos=str(minutos)
aux=aux%60
aux=str(aux)


print(horas+":"+minutos+":"+aux)
