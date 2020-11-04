#RA, Nome, Data de Nascimento, Sexo, Telefone e Email. Cada Aluno possui um RA único
import Menu
def cadastro():
     op = 1
     matriz = []
     i = 0
     while op == 1:
               ra =int(input('Digite o RA do aluno(a):'))
               if ra not in matriz:
                    lista_aluno = []
                    lista_aluno.append(ra)
                    lista_aluno.append(str(input('Digite o nome do aluno(a)')))
                    lista_aluno.append(str(input('Data de nascimento do aluno(a):')))
                    lista_aluno.append(str(input('Digite o sexo do aluno[F/M]:')))
                    lista_aluno.append(int(input('Digite o telefone do aluno(a):')))
                    lista_aluno.append(str(input('Digite o email do aluno(a):')))
                    matriz.append(lista_aluno)
                    print(matriz)
                    op = int(input('Deseja cadastrar um novo aluno 1-sim:'))
               else:
                    if ra in matriz:
                         print('RA encontrado')

cadastro()
