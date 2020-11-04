#Crie uma função que receba como parâmetro um número inteiro. A função
#deve retornar um número inteiro, conforme a seguir:
#a) Retornar 1 se o número recebido é positivo
#b) Retornar -1 se o número recebido é negativo
#c) Retornar 0 se o número recebido é zero
def veri(n):
    if n > 0:
        return(1)
    elif n < 0:
        return(-1)
    else:
        if n == 0:
            return(0)

#__________________________________________________________________________
n = int(input('Digite um número:'))
if veri(n) == 1:
    print('Positivo')
elif veri(n) == -1:
    print('Negativo')
else:
    print('Zero')
