#nome do aluno, idade, notas de português, matemática e ciências


#a) a idade média dos alunos da turma;
#b) o(s) nome(s) do(s) aluno(s)que tiveram a maior nota de matemática;
#c) o(s) nome(s) do(s) aluno(s) que tiveram a menor nota de português;
#d) os nomes dos alunos e suas respectivas médias (médiado aluno entre as três disciplinas)
#em ordem alfabética;
#e) nomes dos alunos e suas respectivas médias (média do aluno entre as três disciplinas)
#em ordem da maior para a menor média

def cadastro():
     lista_geral = []
     total = int(input('Quantos alunos deseja cadastrar:'))
     for i in range(total):
          lista_aluno = []
          lista_aluno.append(str(input('Digite o nome do aluno:')))
          lista_aluno.append(int(input('Digite a idade do aluno:')))
          lista_aluno.append(float(input('Digite a nota de português:')))
          lista_aluno.append(float(input('Digite a nota de matemática:')))
          lista_aluno.append(float(input('Digite a nota de ciências:')))
          lista_geral.append(lista_aluno)
     print(lista_geral)
     media(lista_geral)

def media(lista_geral):
     i = 0
     soma = 0
     cont = 0
     media = 0
     maior = 0
     x = 0
     nome_da_maior_nota=0
     menor = lista_geral[i][2]
     while i<len(lista_geral):
          x = lista_geral[i][1]
          soma = x + soma
          cont = cont + 1
          media = soma/cont
          if lista_geral[i][3]>maior:
               maior = lista_geral[i][3]
          elif lista_geral[i][2]< menor:
                   menor = lista_geral[i][2]
          i = i + 1
          for x in lista_geral:#acesso a matriz
               for y in x:#acesso a cada lista da matriz
                    if y == maior:#se o elemento y for igual a maior
                       nome_da_maior_nota = x[0]#tem que acessar a linha
     print('A idade idade média da turma é:',media)
     print('A maior nota de matemática é:',maior)
     print('A menor nota de português é:',menor)
     print('O nome do aluno com maior nota em matemática:',nome_da_maior_nota)

#_________________________PROGRAMA PRINCIPAL _____________________________

cadastro()
