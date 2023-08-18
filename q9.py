import random
cont=0
while cont<1:  
    mgs=random.randint(1, 35)
    driver=random.randint(1, 35)
    crash=random.randint(1, 35)
    warped=random.randint(1, 35)
    tekken=random.randint(1, 35)
    cortex=random.randint(1, 35)
    ffVIII=random.randint(1, 35)
    ffVII=random.randint(1, 35)
    gran=random.randint(1, 35)
    gran2=random.randint(1, 35)

    print('Tabela de vendas:\n Metal Gear Solid:', mgs,'\nDriver: ',driver,'\nCrash Bandicoot: ',crash,'\nWarped: ',warped,'\nTekken 3: ',tekken,'\nCortex: ',cortex,'\nFinal Fantasy VIII: ',ffVIII,'\nFinal Fantasy VII: ',ffVII,'\nGran Turismo: ',gran,'\nGran Turismo 2: ',gran2)
    if mgs>driver and mgs>crash and mgs>warped and mgs>tekken and mgs>cortex and mgs>ffVIII and mgs>ffVII and mgs>gran and mgs>gran2:
        print('O ganhador foi Metal Gear Solid')
        cont=cont+1
    elif  driver>crash and driver>warped and driver>tekken and driver>cortex and driver>ffVIII and driver>ffVII and driver>gran and driver>gran2:
        print('O ganhador foi Driver')
        cont=cont+1
    elif crash>mgs and crash>warped and crash>tekken and crash>cortex and crash>ffVIII and crash>ffVII and crash>gran and crash>gran2:
        print('O ganhador foi Crash Bandicoot')
        cont=cont+1
    elif warped>mgs and warped>driver and warped>tekken and warped>cortex and warped>ffVIII and warped>ffVII and warped>gran and warped>gran2:
        print('O ganhador foi Warped')
        cont=cont+1
    elif tekken>mgs and tekken>driver and tekken>crash and tekken>cortex and tekken>ffVIII and tekken>ffVII and tekken>gran and tekken>gran2:
        print('O ganhador foi Tekken 3')
        cont=cont+1
    elif cortex>mgs and cortex>driver and cortex>crash and cortex>warped and cortex>ffVIII and cortex>ffVII and cortex>gran and cortex>gran2:
        print('O ganhador foi Cortex')
        cont=cont+1
    elif ffVIII>mgs and ffVIII>driver and ffVIII>crash and ffVIII>warped and ffVIII>tekken and ffVIII>ffVII and ffVIII>gran and ffVIII>gran2:
        print('O ganhador foi Final Fantasy VIII')
        cont=cont+1
    elif ffVII>mgs and ffVII>driver and ffVII>crash and ffVII>warped and ffVII>tekken and ffVII>cortex and ffVII>gran and ffVII>gran2:
        print('O ganhador foi Final Fantasy VII')
        cont=cont+1
    elif gran>mgs or gran>driver and gran>crash and gran>warped and gran>tekken and gran>cortex and gran>ffVIII and gran>gran2:
        print('O ganhador foi Gran Turismo')
        cont=cont+1
    elif gran2>mgs or gran2>driver and gran2>crash and gran2>warped and gran2>tekken and gran2>cortex and gran2>ffVIII and gran2>gran:
        print('O ganhador foi Gran Turismo 2')
        cont=cont+1