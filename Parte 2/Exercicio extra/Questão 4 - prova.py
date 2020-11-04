def insere_aluno():
     notas_alunos = {}
     cont_provas = 0
     op_menu = str(input('Deseja iniciar o cadastro [S/N]:')).upper()
     while op_menu == 'S':
          lista_geral = []
          nome = str(input('Digite o nome do aluno:')).upper()
          if nome in notas_alunos:
               return -1
          else:
               email = str(input('Digite o e-mail do aluno:'))
               op = str(input('Deseja adicionar disciplina ou notas [S/N]:')).upper()
               while op == 'S':
                    lista = []
                    disciplina = str(input('Digite o nome da disciplina:'))
                    nota = float(input('Digite a nota da disciplina:'))
                    cont_provas = cont_provas + 1
                    op = str(input('Deseja adicionar disciplina ou notas [S/N]:')).upper()
                    lista.append(disciplina)
                    lista.append(nota)
                    lista_geral.append(email)
                    lista_geral.append(lista)
                    if op == 'N':
                         notas_alunos[nome] = tuple(lista_geral)
                         print(notas_alunos)
                         print('Foram cadastradas {} provas'.format(cont_provas))
                         op_menu = str(input('Deseja iniciar o cadastro [S/N]:')).upper()
                    if op_menu == 'N':
                         break
                         print('Fim do programa')
                         altera_nota(nome_prova,nova_nota,nome_aluno,notas_alunos,lista)
                         
#_____________________________________________________________________________________________

def altera_nota(nome_prova,nova_nota,nome_aluno,notas_alunos,lista):
     if nome_prova in lista:
          p = lista[1]
          del lista[p]
          lista.insert(p,nova_nota)
          notas_alunos[nome] = tuple(lista[:])
          print(notas_alunos)

#__________________________________________________________________________________
#Chamada da função
insere_aluno()
if insere_aluno() == -1:
     print('Aluno existente no sistema.')
nome_aluno = str(input('Digite o nome do aluno:'))
nome_prova = str(input('Digite o nome da prova:'))
nova_nota = float(input('Digite a nova nota:'))
altera_nota(nome_prova,nova_nota,nome_aluno,notas_alunos,lista)
