#Escrever um programa que permita ao usuário digitar o dia e mês de seu
#aniversário e a data de hoje (dia e mês); em seguida, o programa deve calcular
#quantos dias faltam entre a data de hoje e a data do próximo aniversário. Suponha
#todos os meses com 30 dias
d = int(input('Digite o dia de hoje:'))
m = int(input('Digite o mês [1-Janeiro,2-Fevereiro]:'))

d_aniv = int(input('Digite o dia do aniversário:'))
m_aniv = int(input('Digite o mês do aniversário [1-Janeiro,2-Fevereiro]:'))

if m < m_aniv:
    dias_quebrados = 30 - d + d_aniv
    meses = m_aniv - m - 1 
    total = (meses * 30) + dias_quebrados
    print(total)
else:
    if  m_aniv > m:
        dias_quebrados = 30 + d - d_aniv
        meses =((12 - m)-1) * 30
        total = (meses * 30) + dias_quebrados
        print(total)
