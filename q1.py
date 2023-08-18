import random
jesse_quick=random.randint(1, 300)
barry_allen=random.randint(1, 300)
wally_west=random.randint(1, 300)
dr_wells=random.randint(1, 300)
jay_garrick=random.randint(1, 300)
max_mercury=random.randint(1, 300)
if jesse_quick>barry_allen and jesse_quick>wally_west and jesse_quick>wally_west and jesse_quick>dr_wells and jesse_quick>jay_garrick and jesse_quick>max_mercury:
    print('O vencedor foi Jesse Quick, ou seja: ',jesse_quick*300.000,'Km/s')
elif barry_allen>jesse_quick and barry_allen>wally_west and barry_allen>wally_west and barry_allen>dr_wells and barry_allen>jay_garrick and barry_allen>max_mercury:
    print('O vencedor foi Barry Allen, ou seja: ',barry_allen*300.000,'Km/s')
elif wally_west>jesse_quick and wally_west>barry_allen and wally_west>dr_wells and wally_west>jay_garrick and wally_west>max_mercury:
    print('O vencedor foi Wally West, ou seja: ',barry_allen*300.000,'Km/s')
elif dr_wells>jesse_quick and dr_wells>barry_allen and dr_wells>wally_west and dr_wells>jay_garrick and dr_wells>max_mercury:
    print('O vencedor foi Dr Wells, ou seja: ',barry_allen*300.000,'Km/s')
elif jay_garrick>jesse_quick and jay_garrick>barry_allen and jay_garrick>wally_west and jay_garrick> dr_wells and jay_garrick>max_mercury:
    print('O vencedor foi Jay Garrick, ou seja: ',barry_allen*300.000,'Km/s')
elif max_mercury>jesse_quick and max_mercury>barry_allen and max_mercury>wally_west and max_mercury>dr_wells and max_mercury>jay_garrick:
    print('O vencedor foi Max Mercury, ou seja: ',barry_allen*300.000,'Km/s')
else:
    print('Um empate ocorreu no final da corrida')