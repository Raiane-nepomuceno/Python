N = int(input('Num:'))
#controle incremento fatorial do natural Num N
i = 1
#número harmônico HN = 1+1/2+1/3+1/4...1/N
contador = 0
while N>= 1 and i<=N:
    soma = (1/i)
    contador = contador + soma
    i = i + 1
    
print(contador)
