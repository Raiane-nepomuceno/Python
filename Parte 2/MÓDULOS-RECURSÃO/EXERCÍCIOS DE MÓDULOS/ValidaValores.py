#Valida valores

import string

def ValidaInteiroPositivo(nro):
    for i in nro:
        if i not in string.digits:
            return False
    return True

def ValidaInteiro(nro):
    if nro[0] == '+' or nro[0]=='-':
        nro=nro[1:]
    for i in nro:
        if i not in string.digits:
            return False
    return True

def ValidaReal(nro):

    ponto,positivo,negativo,letras=0,0,0,0

    if nro[0]== ".":
        nro=nro[1:]
        ponto+=1
    elif nro[0]== "+":
        nro=nro[1:]
        positivo+=1
    else:
        if nro[0]== "-":
            nro=nro[1:]
            negativo+=1
 
    for i in nro:
        if i not in string.digits:
            if i==".":
               ponto=ponto+1
            else:
               letras=letras+1

    if letras>0 or positivo>1 or negativo>1 or ponto>1:
       return False
    else:
        return True


