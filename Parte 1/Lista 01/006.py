#6) Escrever um algoritmo para ler as dimensões de uma cozinha (comprimento,
#largura e altura),calcular e escrever a quantidade de caixas de azulejos para
#azulejar todas as paredes (considere que não será descontada a área ocupada
#por portas e janelas). Cada caixa de azulejos possui 2 metros quadrados.
c = float(input('COMPRIMENTO:'))
l = float(input('LARGURA:'))
a = float(input('AlTURA:'))

#calculo
r= (l*c)*2#2 =total ed paredes
s=(a*c)*2
u=(a*l)*2
t = r+s+u
#regra de tres
resp = t /2
print('{} caixas de azulejos'.format(resp))

