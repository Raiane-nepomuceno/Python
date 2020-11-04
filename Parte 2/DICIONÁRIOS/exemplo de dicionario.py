def main():
    print('''
          1-CADASTRAR ALUNO
          2-ATUALIZAR ALUNO
          3-EXCLUIR ALUNO
          4-LISTAR DADOS DE ALUNO
          5-LISTAR TODOS OS ALUNOS
          6-SAIR''')
    
def cadastro(dic_aluno,lista):
    dic_aluno['RA'] = int(input('Digite o RA do aluno:'))
    dic_aluno['Nome'] =str(input('Digite o nome do aluno:'))
    dic_aluno['nasc'] =str(input('Digite a data de nascimento do aluno:'))
    dic_aluno['sexo'] =str(input('Digite o sexo do aluno:'))
    dic_aluno['telefone']=int(input('Digite o telefone do aluno:'))
    dic_aluno['email'] =str(input('Digite o e-mail do aluno:'))
    lista.append(dic_aluno.copy())
    print(lista)

def atualiza(dic_aluno):
    dic_aluno['RA'] = int(input('Digite o RA do aluno:'))
    if dic_aluno['RA'] in dic_aluno:
        print('RA localizado.')
        
def menu_atualiza():
   print('''
         1- Nome
         2- Data de nascimento
         3- Sexo
         4- Email''')
    
def excluir():
    print('''
          1-NOME
          2-DATA DE NASCIMENTO
          3-SEXO
          4-EMAIL
          5-TODOS OS DADOS
          6-SAIR''')
#_____________________________________________________________

lista = []
dic_aluno = {}
cadastro(dic_aluno,lista)
atualiza(dic_aluno)


   
