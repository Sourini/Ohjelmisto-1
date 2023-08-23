sukupuoli = input('oletko mies (m) vai nainen (n)?')
hemoarvo = float(input('anna hemoglobiiniarvosi g/l:'))
if sukupuoli == "m":
    if hemoarvo >= 134 and hemoarvo <= 195:
        print('hemoglobiiniarvosi on ok!')
    elif hemoarvo < 134:
        print('hemoglobiiniarvosi on alhainen')
    else:
        print('hemoglobiiniarvosi on korkealla')
elif sukupuoli == "n":
    if hemoarvo >= 117 and hemoarvo <= 175:
        print('hemoglobiiniarvosi on ok!')
    elif hemoarvo < 117:
        print('hemoglobiiniarvosi on alhainen')
    else:
        print('hemoglobiiniarvosi on korkealla')
else:
    print('error')