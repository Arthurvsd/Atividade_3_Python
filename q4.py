repeticao=1
idademenor=0
idademaior=-1
mulhervelha=''
while repeticao==1:
    nome=str(input('Qual o nome da pessoa? '))
    sexo=int(input('Qual o sexo da pessoa? Digite 1 - para masculino e 2 - para feminino: '))
    idade=int(input('Qual a idade da pessoa? '))
    if sexo==1:
        if idade>idademenor:
            idademenor=idade
    else:
        if idade>idademaior:
            idademaior=idade
            mulhervelha=nome
    repeticao=int(input('Você gostaria de adicionar mais alguém? Escolha entre 1 para Sim ou 2 para Não: '))
    if mulhervelha=='':
        print('Não existe mulher velha.')
    elif idademenor==0:
        print('Não existe homem.')
print('O nome da mulher mais velha é: ',mulhervelha,'e a idade do homem mais novo é:', idademenor)