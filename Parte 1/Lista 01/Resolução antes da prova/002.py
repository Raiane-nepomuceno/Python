cont = 0
for c in range(5):
     num = float(input('Num:'))
     if num > 10:
          cont = cont + 1
print('Há {} números maiores que 10.'.format(cont))
