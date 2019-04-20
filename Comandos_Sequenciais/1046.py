horas=input().split(' ')

hi=int(horas[0])
hf=int(horas[1])

if hf==hi:
    print("O JOGO DUROU 24 HORA(S)")

if hf>hi:
    hf=hf-hi
    print("O JOGO DUROU %d HORA(S)" %hf)

if hf<hi:
    hi=(24-hi) + hf
    print("O JOGO DUROU %d HORA(S)" %hi)
    
