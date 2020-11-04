# fev --- 28 dias
# jan,julh,nov,dez --- 31 dias
d = int(input('Digite o dia:'))
m = int(input('Digite o mês [1-Janeiro,2-Fevereiro]:'))
dias = 360
# estou encontrando o num de dias referentes ao periodo
r = dias/m - d
# apos encontrar o num de dias(360) calculamos a quant de dias para o final do ano
print('Faltam {} dias para o fim do ano'.format(r))
if m == 2:#desconta para chegar nos 28 dias (30-2)
    print(r-2)
else:
    if m == 1 or m == 7 or m == 11 or m == 12:#desconta para chegar nos 31 dias (30+1)
        print(r+1)
        


