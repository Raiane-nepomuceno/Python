odo_dia = int(input('Marcação do odomêtro no início do dia:'))
marc = int(input('marcação no final do dia:'))
litro = float(input('Litros de combustível gasto:'))
real = float(input('O valor de R$ recebido dos passageiros:'))
#Calcule e escreva   a média do consumo em Km/l
#e o lucro líquido do dia. Se o lucro  líquido
#no  dia  for  inferior  a  R$  100,00  exiba
#a  mensagem  que  o  taxista precisa melhorar
#seu desempenho.
valortotal = float(input('Informe o valor recebido pelo passageiro:'))

cartao = int(input('Deseja pagar no cartão de crédito ou débito[1-sim/2-nao]:'))

dinheiro = int(input('Deseja pagar no dinheiro [1-sim/2-nao]:'))

cheque = int(input('Deseja pagar no cheque [1-sim/2-nao]:'))

media = (odo_dia + marc)/2
lucro = real - (2.50*litro)
print(lucro)
