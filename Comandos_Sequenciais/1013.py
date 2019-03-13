numeros=input().split(' ')
a=int(numeros[0])
b=int(numeros[1])
c=int(numeros[2])
MaiorAB=(a+b+abs(a-b))/2

MaiorDeTodos=int((MaiorAB+c+abs(MaiorAB-c))/2)

print(MaiorDeTodos,"eh o maior")
