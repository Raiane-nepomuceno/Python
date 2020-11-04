def leitura():
    nro = int(input('Número:'))
    return(nro)
def soma(n1,n2):
    return n1+n2

def subtraia(n1,n2):
    return(n1-n2)

def multiplique(n1,n2):
    return n1*n2

def divida(n1,n2):
    return n1/n2

#------------------------------------------------------
#Programa Principal
def main():
    op = input('Escola uma operação(+,-,*,/):')
    nro1 = leitura()
    nro2 = leitura()
    if op == '+':
        print(soma(n1,n2))
    elif op =='-':
        print(subtraia(nro1,nro2))
    elif op =='*':
        print('Multiplicação:',multiplique(nro1,nro2))
    elif op =='/':
        print('Divisão:',divida(nro1,nro2))
    else:
        print('Operação inválida')
main()
