import random

print(' ----------- Bem vindo ao Jogo da Advinha ----------')
print() 
print('O jogador tem que advinhar qual o número de 1 a 100, e tem 7 vidas. BOA SORTE! ')
print()

numeroAleatorio = random.randint(1,100)

tentativa = ""
opcao = ""
vidas = 7
vidasrest = vidas

while vidas > 0 and opcao != "S" and tentativa != numeroAleatorio: 
    tentativa = int(input('Diga um número: '))
    
    if tentativa != numeroAleatorio:
        vidas = vidas - 1
        vidasrest
        print('Errou! Tente outra vez, tem ', vidas, 'tentativas')
        
        if vidas > 0:
            diferenca = abs(numeroAleatorio - tentativa)
        
            if diferenca <= 1:
                print('Está perto!')
            else:
                print('Está longe!')
            
        if vidas == 0:
            print('GAME OVER, ficou sem vidas! :/ ')
            print('O número é: ' ,numeroAleatorio)
        else:            
            opcao = input('Deseja sair? (S/N) ').upper()
         
    else:
        print('PARABÉNS!! ACERTOU!!! Usou' , 2 - vidasrest, 'tentativa(s)! :D')
         