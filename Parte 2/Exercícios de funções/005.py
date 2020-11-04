#Faça uma função que receba quatro valores, referentes as notas que um aluno
#obteve nos bimestres. A função deve retornar Verdadeiro se o aluno foi
#aprovado e Falso caso contrário.
def media(a,b,c,d):
    soma = (a+b+c+d)/4
    if soma>=6:
        return True
    else:
        return False

#____________________PROGRAMA PRINCIPAL___________________
a = float(input('Digite a primeira nota:'))
b = float(input('Digite a segunda nota:'))
c = float(input('Digite a terceira nota:'))
d = float(input('Digite a quarta nota:'))
if media(a,b,c,d) == True:
    print('Aprovado')
else:
    print('Reprovado')
