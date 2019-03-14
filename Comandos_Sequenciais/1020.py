idade=int(input())

ano=idade//365
aux=idade%365

mes=aux//30
aux=aux%30


print(ano, "ano(s)")
print(mes,"mes(es)")
print(aux, "dia(s)")
