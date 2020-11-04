p = float(input('A nota da prova:'))
t = float(input('A nota do trabalho:'))
f = float(input('A frequência do aluno:'))
m = ((p*7)+(t*3))/10
if m>= 6 and f>=75:
     print('Aprovado')
elif m>=4 and m <6 and f>=75:
     print('Recuperação')
else:
     print('Reprovado')
