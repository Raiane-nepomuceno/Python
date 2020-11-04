#entrada de dados: marcação do odômetro no início do dia
odometroinicial = float(input('Informe a marcação do odômetro no início do dia:'))

#entrada de dados: marcação de odômetro no fim do dia
odometrofinal = float(input('Informe a marcação do odômetro no fim do dia:'))

#quant de litros gastos
numerocomb = float(input('Informe o número de litros de combustível gasto:'))

#valor pago pelo passageiro
valortotal = float(input('Informe o valor recebido pelo passageiro:'))

cartao = int(input('Deseja pagar no cartão de crédito ou débito[1-sim/2-nao]:'))

dinheiro = int(input('Deseja pagar no dinheiro [1-sim/2-nao]:'))

cheque = int(input('Deseja pagar no cheque [1-sim/2-nao]:'))

# ---> Fórmulas:

media_consumo = (odometroinicial+odometrofinal)/2
din =  valortotal - (5 * valortotal)/100
cart =  valortotal - (2 * valortotal)/100 
cheq = (10*valortotal)/100 + valortotal
lucro = valortotal - (2.50 * numerocomb)

print('A média do consumo em Km/l:',media_consumo)
print('O lucro do dia foi:',lucro)

if lucro < 100:
    print('Precisa melhorar o desempenho')
    
else:
    if lucro > 120 and lucro < 150:
        print('Desempenho bom!')
    if lucro > 159 and lucro < 200:
        print('Excelente corrida!')
        
if cartao == 1:
    print('O valor da corrida paga no cartão de créditos ou débito:',cart)
if dinheiro == 1:
    print('O valor da corrida paga em dinheiro:',din)
if cheque == 1:
    print('O valor da corrida paga em cheque:',cheq)



    
        
