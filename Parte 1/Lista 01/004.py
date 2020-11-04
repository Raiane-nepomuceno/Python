#prova 70% trabalho = 30%
n1 = float(input('Digite a nota da prova:'))
n2 = float(input('Digite a nota do trabalho:'))
f = int(input('Digite a frequência do aluno:'))
m = (n1 * 7 + n2 * 3) /(7+3)
#print(m)
if m >= 6 and f >= 75:
    print('Aprovado')
elif m >= 4 and m < 6 and f >= 75:
     print('Recuperação')
else:
    print('Reprovado')
           
