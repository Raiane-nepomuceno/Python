#18) Escreva um programa que permita ao usuário digitar a idade,
#o sexo, e o salário de  um  indivíduo.  Analise  os  dados  de
#entrada  e  imprima  uma  das  possíveis mensagens abaixo: -
#Masculino, com mais de 18 anos. -  Feminino, com salário acima

#de R$ 50.000,00 e com idade acima de 40 anos. -  Masculino ou feminino
#e  idade entre 20 e 30 anos. -  Não se encaixa em nenhuma das possibilidades anteriores.
idade = int(input('Informe a idade:'))
sexo = str(input('Informe o sexo [F/M]:')).upper()
salario = float(input('Informe o salário:'))

if sexo == 'M' and idade > 18:
     print('Masculino,com mais de 18 anos.')
elif sexo == 'F' and idade > 40 and salario > 50.000:
     print('Feminino,com salário acima de R$50.000,00 e com idade acima de 40 anos.')
elif sexo == 'F' or sexo == 'M' and idade >= 20 and idade <=30:
     print(' Masculino ou feminino e  idade entre 20 e 30 anos')
else:
     print('Não se encaixa em nenhuma das possibilidades anteriores.')


