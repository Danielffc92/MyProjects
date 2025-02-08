import random

print('---------------- Jogo da SELVA AMAZÓNICA!! ----------------')
print()

print('Neste jogo o jogador és um explorador em busca de um tesouro lendário numa ilha misteriosa! :D')
print()


tesouro = random.choice(["Sim" , "Nao"])

decisao = str(input('Queres seguir com esta aventura? (S/N) ')).upper()


if decisao == 'S':
    print('Tomaste a decisão certa!! Vamos continuar, Aventureiro!')
    print()
    print('Chegaste a uma Ponte!')
    
    ponte = str(input('Queres cruzar esta ponte instável? (S/N) ')).upper()
    
    if ponte == 'S':
        print('Vai com cuidado aventureiro, esta ponte pode ser perigosa! ')
    else:
        print('CUIDADO!!! VEM UM TIGRE NA TUA DIREÇÃO!! CORREEEEEE!!!!')
    print()
    print('Chegaste a uma clareira!')
    
    clareira = str(input('Esta clareira parece perigosa, estamos muito expostos! Vamos continuar? (S/N) ')).upper()
    
    if clareira == 'S':
        print('Vamos em frente! Parece que temos um caminho mais a diante!')
    else:
        print('Olha que aqui estamos expostos a possiveis ameaças! Volta para trás!')
    print()    
    print('Chegaste a uma caverna!')    
    
    caverna = str(input('Esta caverna tem um ar super sinistro, queres continuar? (S/N) ')).upper()
    
    if caverna == 'S':
        print('Agarra na tua lanterna e vamos a esta aventura! Cuidado com os Morcegos! :P')
    else: 
        print('CUIDADO VAIS TE PERDER NA SELVA!!!')
    print()
     
    caminho = str(input('Chegamos a uma bifurcação queres ir para a esquerda ou para a direita? (E/D) ')).upper()
    
    if caminho == 'D':
        print('Escolheste o caminho do lado direito!!!')
    else:
        print('Escolheste o caminho do lado esquerdo!!!')
    print()
    
    if tesouro == "Sim":
        print('CONSEGUIU O TESOURO! PARABÉNS!! :D')
    else:    
        print('OH!! Não conseguiu ganhar o tesouro! :( Tente numa próxima aventura!)')
      

else:
    print('Volta quando quiseres jogar! :D')

