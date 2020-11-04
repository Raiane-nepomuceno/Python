from random import randint
from time import sleep

#Pergunta que terá controle do laço

op = int(input('Deseja iniciar o jogo [1]sim,[2]não:'))

#declração das variávies

soma = 0
vidas = 5 #total de vidas
total = 0
if op == 1:
#Parte inicial - configurações do game
    print('-='*20)
    print('CARREGANDO...')
    sleep(2)
    print('VA')
    sleep(2)
    print('LEN')
    sleep(2)
    print('DO!!!')
    sleep(2)
    print('-='*10)
    print('FASE 1')
    print('-='*10)
    print('''MÁRIO,ESTÁ GRANDE
    [1]ANDAR
    [2]PULAR
    [3]SAIR DO JOGO''')
while op == 1:#enqu
        jogador = int(input('QUAL É A SUA JOGADA:'))
        itens = ('Cogumelo verde','Flor','Pena','Cogumelo vermelho','Tamanho','Capa','Estrela','Tartaruga','Fogo e capa','Moeda','Buraco')
        computador = randint(0,10)
        #Possibilidades do jogador e computador jogarem    
        if computador == 0:#computador jogou cogumelo,Mário pegou o cogumelo
            if jogador == 1:#andou
                soma = soma - 40
                print('OPS,MÁRIO PEGOU O COGUMELO VERDE.')
            elif jogador == 2:#pulou
                print('MÁRIO,DESVIOU DO COGUMELO!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
    
        if computador == 1:#flor 
            if jogador == 1:
                soma = soma + 10
                print('MÁRIO,PEGOU A FLOR!')
            elif jogador == 2:
                print('MÁRIO,DESVIOU DA FLOR!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if computador == 2: #pena
            if jogador == 1:
                soma = soma + 20
                print('MÁRIO,PEGOU A PENA!')
            elif jogador == 2:
                print('MÁRIO,DESVIOU DA PENA!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if computador == 3: #cogumelo vermelho
            if jogador == 1:
                print('MÁRIO,PEGOU O COGUMELO VERMELHO!')
                soma = soma - 100
            elif jogador == 2:
                print('MÁRIO,DESVIOU DO COGUMELO VERMELHO!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if computador == 4: #tamanho
            if jogador == 1:
                print('MÁRIO ESTÁ GRANDE!')
                soma = soma + 10
            elif jogador == 2:
                print('MÁRIO ESTÁ PEQUENO!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if computador == 5: #capa
            if jogador == 1:
                print('MÁRIO PEGOU A CAPA!')
                soma = soma + 20
            elif jogador == 2:
                print('MÁRIO DESVIOU DA CAPA!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')

        if computador == 6: #estrela
            if jogador == 1:
                print('MÁRIO ESTÁ GRANDE!')
                soma = soma + 30
            elif jogador == 2:
                print('MÁRIO ESTÁ COM A ALTURA NORMAL!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')

        if computador == 7: #tartaruga
            if jogador == 1:
                print('MÁRIO TEM O PODER DA TARTARUGA!')
                soma = soma + 50
            elif jogador == 2:
                print('MÉRIO DESVIOU DO PODER!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')

        if computador == 8: #fogo e capa
            if jogador == 1:
                print('MÁRIO ESTÁ COM O FOGO E A CAPA')
                soma = soma + 60
            elif jogador == 2:
                print('MÁRIO DESVIOU DO PODER')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')

        if computador == 9: #moeda
            if jogador == 1:
                print('MÁRIO PEGOU UMA MOEDA!')
                soma = soma + 5
            elif jogador == 2:
                print('MÁRIO DESVIOU DA MOEDA!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if computador == 10: #buraco
            if jogador == 1:
                print('MÁRIO CAIU NO BURACO!')
                soma = soma - 10
            elif jogador == 2:
                print('MÁRIO DESVIOU DO BURACO.BOA JOGADA!')
            else:
                print('OPÇÃO INVÁLIDA.TENTE NOVAMENTE!')
        if jogador == 3:
            print('-='*15)
            print('PONTUAÇÃO FINAL FOI:',soma)
            print('FIM DO JOGO')    


    #controle da soma ou seja o total dos pontos
            
        if soma < 0:#se a soma for menor que 0
            vidas = vidas - 1 #as vidas vão diminuindo assim que chegar na pontuação negativa
            soma = 0
            print('-='*20)
            print('MÁRIO PERDEU UMA VIDA.')
            print('RESTAM {} VIDAS'.format(vidas))
        if vidas == 0:
            print('-='*20)
            print('ACABARAM AS VIDASS...')
            print('FIM DO JOGO.TENTE NOVAMENTE!')
            print('-='*20)
            break
        if soma>=100 and soma<= 135:
            print('-='*20)
            print('FASE CONCLUÍDA COM SUCESSO.')    
            print('PONTUAÇÃO FINAL FOI:',soma)
            print('-='*20)
            break

