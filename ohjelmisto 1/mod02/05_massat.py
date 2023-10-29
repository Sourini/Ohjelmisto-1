leiviska = float(input('anna leiviskät: '))
naula = float(input('anna naulat: '))
luoti = float(input('anna luodit: '))
gramma = 13.3*(luoti+(32*naula)+(32*20*leiviska))
kilogramma = gramma//1000
vitunscuffedgrammat = gramma-(kilogramma*1000)
print(f"Massa nykymittojen mukaan:\n{kilogramma:.0f}kg ja {vitunscuffedgrammat:.2f}g")