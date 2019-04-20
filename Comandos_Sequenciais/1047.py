tempo=input().split(' ')

hi=int(tempo[0])
mi=int(tempo[1])
hf=int(tempo[2])
mf=int(tempo[3])


if hf > hi:
    
    if mf==mi:
        hf=hf-hi
        print("O JOGO DUROU %d HORA(S) E 0 MINUTO(S)" %hf)

    elif mf>mi:
        hf=hf-hi
        mf=mf-mi
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hf,mf))

    elif mf<mi:
        hf=hf-hi
        mf=60-mi+mf
        if mf<=59 and hf==1:
            print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)" %mf)
        else:
            print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hf,mf))
            
#----------------------------------------------------------------------------

elif hf == hi:
    
    if mf>mi:
        mf=mf-mi
        print("O JOGO DUROU 0 HORA(S) E %d MINUTO(S)" %mf)

    elif  mf == mi:
        print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")

#----------------------------------------------------------------------------


elif hf < hi:

    if mf>mi:
        hf = 24-hi+hf
        mf = mf-mi
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hf,mf))
   
    elif mf == mi:
        hf = 24-hi+hf
        print("O JOGO DUROU %d HORA(S) E 0 MINUTO(S)" %hf)

    elif mf<mi:
        mf=60-mi+mf
        hf = 23-hi+hf
        print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" %(hf,mf))
        

