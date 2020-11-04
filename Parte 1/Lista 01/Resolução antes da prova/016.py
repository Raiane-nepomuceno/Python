d=int(input('Dia:'))
m=int(input('Mês:'))
dias = 360
r = 360/m-d
print('DIAS PARA O FIM DO ANO:',r)
if m == 2:
     print(r-2)
else:
     if m == 1 or m == 7 or  m ==12 or m == 11:
          print(r+1)
     
