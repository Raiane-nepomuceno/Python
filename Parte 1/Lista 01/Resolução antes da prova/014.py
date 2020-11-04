i = int(input('Idade:'))
if i < 16:
     print('Não eleitor')
elif i>=18 and i<65:
     print('Obrigatório')
else:
     if i>=16 and i<18 or i>65:
          print('Facultativo')
     
