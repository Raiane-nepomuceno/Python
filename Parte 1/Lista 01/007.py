s = float(input('Salário bruto do funcionário:'))
p = float(input('Valor da prestação desejada:'))
med = s*(30/100)
if  p <= med:
    print('Emprétimo aprovado!')
else:
    print('Empéstimo negado,valor alto!')
