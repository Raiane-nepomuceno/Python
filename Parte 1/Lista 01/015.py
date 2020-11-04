nome = str(input('Digite o nome da pessoa:'))
n=int(input('Digite a idade da pessoa:'))
if n >= 18 and n < 65:
    print('{} é maior de idade.'.format(nome))
elif n < 18:
    print('{} é menor de idade.'.format(nome))
else:
    print('{} é uma pessoa de idade.'.format(nome))

