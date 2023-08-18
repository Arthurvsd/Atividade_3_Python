import random
lokipeso=float=random.randint(0, 100)
volstaggpeso=random.randint(0, 100)
print('O peso de Loki foi: ',lokipeso,'Kg, já o de Volstagg foi: ', volstaggpeso,'Kg')
if lokipeso>volstaggpeso:
    print('Loki ganhou!')
else:
    print('Volstagg ganhou a batalha de pesos!')
lokimira=int=random.randint(0, 60)
frandalmira=int=random.randint(0, 60)
if lokimira>frandalmira:
    print('Loki acertou o tiro ao alvo, acertou no ', lokimira)
elif lokimira==0:
    print('Loki acertou no centro!')
elif frandalmira==0:
    print('Frandal acertou no centro!')
else:
    print('Frandal acertou o tiro ao alvo, acertou no ', frandalmira)
lokipolegar=int=random.randint(1, 2)
hogunpolegar=int=random.randint(1, 2)
if lokipolegar>hogunpolegar:
    print('Loki ganhou a batalha de polegares! Pois tirou:', lokipolegar)
else:
    print('Hogun ganhou a batalha de polegares! Pois tirou:', hogunpolegar)

n1=int=random.randint(1, 20)
n2=int=random.randint(1, 20)
n3=int=random.randint(1, 20)
n4=int=random.randint(1, 20)
n5=int=random.randint(1, 20)
n6=int=random.randint(1, 20)
if n1==n2 or n2==n3 or n3==n4 or n4==n5 or n5==n6:
    print(print(n1,n2,'/',n3,n4,'/',n5,n6))
    print('Loki ganhou a batalha contra Valquíria!')

n7=int=random.randint(1, 20)
n8=int=random.randint(1, 20)
n9=int=random.randint(1, 20)
n10=int=random.randint(1, 20)
n11=int=random.randint(1, 20)
n12=int=random.randint(1, 20)
if n7==n8 or n8==n9 or n9==n10 or n10==n11 or n11==n12:
    print(n7,n8,'/',n9,n10,'/',n11,n12)
    print('Valquíria ganhou a batalha contra Loki!')

cont=0
while cont<=3:
    atacante=int=random.randint
    if atacante%2==0:
        print('O atacante gerou o número:',atacante)
        defensor=int=random.randint
        if defensor%2==1:
            print('O defensor gerou o número:', defensor)