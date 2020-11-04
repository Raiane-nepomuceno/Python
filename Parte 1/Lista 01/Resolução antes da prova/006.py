c = float(input('Comprimento:'))
l = float(input('Largura:'))
a = float(input('Altura:'))
t = (c*l)*2
s = (a*c)*2
u = (a*l)*2
resp = (t+s+u)/2
print('{} caixas de azulejos'.format(resp))
