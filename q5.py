import random
cont=0
moto=0
onibus=0
carro=0
while cont<=400:
    veiculos=random.randint(1, 3)
    if veiculos==1:
        moto=moto+1
    elif veiculos==2:
        onibus=onibus+1
    elif veiculos==3:
        carro=carro+1
    cont=cont+1
print('A quantidade de dinheiro do dia foi: ',moto*4+onibus*20+carro*8)