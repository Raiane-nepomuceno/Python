d=int(input('Dia de hoje:'))
m=int(input('Mês:'))

d_aniv = int(input('Dia do niver:'))
m_aniv = int(input('Mês do niver:'))

if m<m_aniv:
     dias_quebrados = 30 - d + d_aniv
     meses =m_aniv -m -1
     total =(meses*30) + dias_quebrados
     print(total)
elif m == m_aniv:
     total = d_aniv - d
     print(total)
else:
     if m_aniv>m:
          dias_quebrados = 30+d-d-aniv
          meses =((12-m)-1)*30
          total =(meses*30)+ dias-quebrados
          print(total)
