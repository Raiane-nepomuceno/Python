#Faça uma função que receba quatro valores reais, referentes as notas que um
#aluno obteve nos bimestres. A função deve retornar a média final desse aluno

def media(a,b,c,d):
    soma = (a+b+c+d)/4
    return soma




#______________________________________Programa Principal _____________________________________

a = float(input('Digite a primeira nota:'))
b = float(input('Digite a segunda nota:'))
c = float(input('Digite a terceira nota:'))
d = float(input('Digite a quarta nota:'))
print(media(a,b,c,d))
