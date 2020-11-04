a = str(input('Digite a primeira string:'))#cpf xxx.xxx.xxx
b = str(input('Digite a segunda string:'))#data de nasc aa/aa/aaaa->1900-2000
c = str(input('Digite a terceira string:'))

c = c.replace(' ','')
a = a.replace(' ','')
print(int(b[0:2]))

#if a[3]=='.' and a[7]=='.' and a[11]=='-' :
 #   print('CPF é válido')
#else:
 #   print('CPF inválido')
if c[::-1] == c[:]:
    print('É um palíndromo ')
#else:
 #   print('Não é um palíndromo.')
#else:
#    print('CPF inválido') 
   




