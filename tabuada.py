import random

print(' --------- Bem-vindo ao Tabuadex! ---------')
print()

print('Neste jogo tens que responder a perguntas da Tabuada, por cada resposta certa ganhas 10 pontos, por cada resposta errada perdes 5.')
print('Tens 10 perguntas aleatórias para responder caso tenhas pontuação positiva ganhas o jogo, senão aconselhamos-te a estudar mais!')
print()


pontos = 0
numerodeperguntas = 10


for numero in range(numerodeperguntas):
    
    numero1 = random.randint(1,10)
    numero2 = random.randint(1,10)
    
    print('Qual a solução desta multiplicação?')
    
    resposta = int(input((f'{numero1} x {numero2} = '))) 
        
    solucao = numero1 * numero2
        
    if resposta == solucao:
        pontos += 10
        print('Resposta correcta! Ganhas-te 10 pontos')
        print(f'Tem {pontos}')
    else:
        pontos -=5
        print('Resposta errada! Perdeste 5 pontos')
        print(f'Tem {pontos}')

if pontos > 0:
    print(f'Parabéns conseguiste {pontos} pontos. Ganhaste o jogo!')
else: 
    print(f'OUPS!! Tens que estudar mais!! Acabaste com {pontos} pontos.')