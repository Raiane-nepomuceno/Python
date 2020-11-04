for i in range(0,1):
    l = float(input('Digite a quantidade de lados do terreno:'))
    c = float(input('Digite o comprimento do terreno:'))
    cid = str(input('Digite a cidade que está localizada o lote [SP/Curitiba]:')).upper()
    m = l*c
    if cid == 'SP':
        sp = 500*m
        print('Em São Paulo custa R${}'.format(sp))
    elif cid == 'CURITIBA':
        curi = 450*m
        print('Em Curitiba custa R${}'.format(curi))
    else:
        print('A cidade não foi localizada')
