kantastr = input('anna suorakulmion kanta: ')
kanta = float(kantastr)
korkeusstr = input('anna suorakulmion korkeus: ')
korkeus = float(korkeusstr)
piiri = kanta*2+korkeus*2
pintaala = kanta*korkeus
print("suorakulmion piiri on " + str(piiri) + "\nsuorakulmion pinta-ala on " + str(pintaala))