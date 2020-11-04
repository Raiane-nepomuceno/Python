lista = []
soma = 0
n = int(input('Digite a quantidade de notas que serão digitadas:'))
for i in range(0,int(n)):
     n = float(input('Digite a nota do aluno:'))
     lista.append(n)
     soma = soma + n
     m = soma/len(lista)
print('A média do aluno é:',m)
     
