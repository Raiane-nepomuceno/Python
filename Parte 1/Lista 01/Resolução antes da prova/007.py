s = float(input('Salário bruto:'))
p = float(input('Valor da prestação desejada:'))
r = s*(30/100)
if p <= r:
     print('Pode ser concedido!')
else:
     print('Não pode ser concedido!')
