num=0
numd=0*-1
sinal=0
for i in range(1,51):
    num+=1
    numd+=-1
    if sinal==0:
        print(numd)
        sinal=1
    elif sinal==1:
        print(numd)
        sinal=2
    elif sinal==2:
        print(num)
        sinal=3
    elif sinal==3:
        print(num)
        sinal=0
print('A soma de tudo dá: ',num-1)