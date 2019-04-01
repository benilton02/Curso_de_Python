lista=input().split(' ')

a=int(lista[0])
b=int(lista[1])
c=int(lista[2])

p=a
s=b
t=c

if c<b and c<a:
    if b<a:
        print(c)
        print(b)
        print(a)
    if b>a:
        print(c)
        print(a)
        print(b)

if b<c and b<a:
    if a<c:
        print(b)
        print(a)
        print(c)
    if a>c:
        print(b)
        print(c)
        print(a)

if a<b and a<c:
    if b<c:
        print(a)
        print(b)
        print(c)
    if b>c:
        print(a)
        print(c)
        print(b)

print()
print(p)
print(s)
print(t)
