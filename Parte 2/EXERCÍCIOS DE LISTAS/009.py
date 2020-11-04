#maior nota de mat
maior = 0
x = 0
soma = 0
i = 0
j=0
cont = 0
matriz = []
quant = int(input('Digite a quantidade de alunos:'))
while i<quant:
     alunos = []
     alunos.append(str(input('Digite o nome do aluno:')))
     alunos.append(int(input('Digite a idade do aluno:')))
     alunos.append(int(input('Digite a nota de português do aluno:')))
     alunos.append(int(input('Digite  a nota matemática do aluno:')))
     alunos.append(int(input('Digite a nota de ciências do aluno:')))
     matriz.append(alunos)
     i=i+1
while j<len(matriz):
     x = matriz[j][1]
     soma = matriz[j][1] + soma
     cont = cont + 1
     m = soma/cont
     if matriz[j][3] > maior:
          maior = matriz[j][3]
          
     j = j + 1
print('Média  das idades dos alunos da turma:',m)
print('Maior nota de matemática foi:',maior,'o estudante que tirou essa nota foi:',nome)
