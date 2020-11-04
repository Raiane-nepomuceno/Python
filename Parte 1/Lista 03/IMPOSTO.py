s = float(input('Salário:'))

if s >= 3000:
    r = s*(35/100)
    print('O imposto é:',r)
elif s <= 1000:
    r = s*(10/100)
    print('O imposto é:',r)
elif s >1000 and s < 3000:
    r = s*(15/100)
    print('O imposto é:',r)
