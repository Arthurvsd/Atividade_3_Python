base=int (input('Digite a base: '))
expoente=int (input('Digite o expoente'))
cont=1
res=base

if expoente==0:
    print('O resultado é 1.')
else:
    while cont<expoente:
        res=res*base
        cont+=1
        print('O resultado da potência é:', res)