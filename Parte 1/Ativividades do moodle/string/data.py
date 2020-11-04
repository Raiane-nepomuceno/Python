a = str(input('Digite a primeira string[xxx.xxx.xxx-xx]:'))#cpf xxx.xxx.xxx
b = str(input('Digite a segunda string[aa/aa/aaaa]:'))#data de nasc aa/aa/aaaa->1900-200
c = str(input('Digite a terceira string[palíndromo]:'))
#Testes do fatiamento:
#print(int(b[0:2]))
#print(int(b[4:5]))
#print(int(b[6:11])) 
c = c.replace(' ','')
b = b.replace(' ','')
a = a.replace(' ','')

if a[3]=='.' and a[7]=='.' and a[11]=='-' :
    print('CPF:{} é válido.'.format(a))
else:
    if a[3]!='.' or a[7]!='.' or a[11]!='-':
        print('CPF:{} inválido.'.format(a))
        
if (int(b[0:2])>31 or int(b[0:2])< 0) or (int(b[4:5])>12 or int(b[4:5])<0) or (int(b[6:11])<1900 or int(b[6:11])>2020):
        print('A data: {} está inválida.'.format(b))
        
else:
    print('A data: {} está correta'.format(b))
if c[::-1] == c[:]:
    print('A palavra: {} é um palíndromo.'.format(c))
else:
    if c[::-1]!=c[:]:
        print('A palavra: {} não é um palíndromo'.format(c))


